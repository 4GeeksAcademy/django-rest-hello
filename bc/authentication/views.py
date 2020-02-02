from django.shortcuts import render
from django.db.models import Q, F
from django.http import HttpResponse
from django.utils import timezone
from jwt.exceptions import DecodeError, ExpiredSignatureError
from bc.utils.notifier import get_template_content

from rest_framework import status
from rest_framework.exceptions import PermissionDenied
from rest_framework.permissions import (
    AllowAny, IsAuthenticatedOrReadOnly, IsAdminUser
)
from rest_framework.response import Response
from rest_framework.serializers import ValidationError
from rest_framework.views import APIView
from rest_framework_jwt.settings import api_settings

from .models import User
from .serializers import UserLoginSerializer, ChangePasswordSerializer, UserRegisterSerializer, UserSerializer

jwt_decode_handler = api_settings.JWT_DECODE_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

class ValidateEmailView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        token = request.GET.get('token')

        try:
            payload = jwt_decode_handler(token)
        except (DecodeError, ExpiredSignatureError) as e:
            return html_error('Your email validation link has expired, please resend it and try again')

        try:
            user = User.objects.get(id=payload["user_id"])
            if user.profile.status != 'PENDING_EMAIL_VALIDATION':
                return html_error(
                    'Your email has been already activated, open the JobCore App and go ahead and sign in')

            try:
                # db_token = UserToken.objects.get(token=token, email=user.email)
                # db_token.delete()

                user.profile.status = 'ACTIVE'  # email validation completed
                user.profile.save()

                template = get_template_content('email_validated')
                return HttpResponse(template['html'])

            except UserToken.DoesNotExist:
                return html_error('Your email validation link has expired, please resend it and try again')

        except User.DoesNotExist:
            return html_error('Not found')


class PasswordView(APIView):
    permission_classes = (AllowAny,)

    def get(self, request):

        token = request.GET.get('token')
        try:
            data = jwt_decode_handler(token)
        except DecodeError as e:
            return html_error('Invalid Token')

        try:
            user = User.objects.get(id=data['user_id'])
        except User.DoesNotExist:
            return html_error('Email not found on the database')

        token = bc.utils.jwt.internal_payload_encode({
            "user_email": user.email,
            "user_id": user.id
        })
        template = get_template_content(
            'reset_password_form', {
                "email": user.email, "token": token})
        return HttpResponse(template['html'])

    def post(self, request):
        email = request.data.get('email', None)
        if not email:
            return Response(
                validators.error_object('Email not found on the database'),
                status=status.HTTP_400_BAD_REQUEST)

        try:
            user = User.objects.get(email=email)
            serializer = UserLoginSerializer(user)
        except User.DoesNotExist:
            return Response(
                validators.error_object('Email not found on the database'),
                status=status.HTTP_404_NOT_FOUND)

        tokenDic = {"token": notify_password_reset_code(user)}

        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request):

        serializer = ChangePasswordSerializer(
            data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ValidateSendEmailView(APIView):
    permission_classes = [AllowAny]

    def post(self, request, email=None):

        if email is None:
            raise ValidationError('Invalid email to validate')

        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return Response(validators.error_object(
                'The user was not found'), status=status.HTTP_400_BAD_REQUEST)

            if user.profile.status != 'PENDING_EMAIL_VALIDATION':
                return Response(validators.error_object('This user is already validated'),
                                status=status.HTTP_400_BAD_REQUEST)

        notify_email_validation(user)

        return Response({"details": "The email was sent"}, status=status.HTTP_200_OK)

class UserRegisterView(APIView):
    permission_classes = [AllowAny]

    serializer_class = UserSerializer

    def post(self, request):
        token = None
        if "token" in request.data:
            token = request.data["token"]

        serializer = UserRegisterSerializer(
            data=request.data,
            context={"token": token})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request, id):
        try:
            user = User.objects.get(id=id)
            serializer = user_serializer.UserGetSerializer(user)
        except User.DoesNotExist:
            return Response(validators.error_object(
                'The user was not found'), status=status.HTTP_404_NOT_FOUND)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, id):
        permission_classes = [IsAdminUser]

        try:
            user = User.objects.get(id=id)
        except User.DoesNotExist:
            return Response(validators.error_object(
                'The user was not found'), status=status.HTTP_404_NOT_FOUND)

        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, id):
        permission_classes = [IsAdminUser]

        try:
            user = User.objects.get(id=id)
        except User.DoesNotExist:
            return Response(validators.error_object(
                'The user was not found'), status=status.HTTP_404_NOT_FOUND)

        serializer = user_serializer.ChangePasswordSerializer(
            data=request.data)
        if serializer.is_valid():
            if serializer.data.get("new_password"):
                # Check old password
                if not user.check_password(
                        serializer.data.get("old_password")):
                    return Response({
                        "old_password": ["Wrong password."]
                    }, status=status.HTTP_400_BAD_REQUEST)
                # Hash and save the password
                user.set_password(serializer.data.get("new_password"))
            user.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        permission_classes = [IsAdminUser]

        try:
            user = User.objects.get(id=id)
        except User.DoesNotExist:
            return Response(validators.error_object(
                'The user was not found'), status=status.HTTP_404_NOT_FOUND)

        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class ValidateSendEmailView(APIView):
    permission_classes = [AllowAny]

    def post(self, request, email=None):

        if email is None:
            raise ValidationError('Invalid email to validate')

        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return Response(validators.error_object(
                'The user was not found'), status=status.HTTP_400_BAD_REQUEST)

            if user.profile.status != 'PENDING_EMAIL_VALIDATION':
                return Response(validators.error_object('This user is already validated'),
                                status=status.HTTP_400_BAD_REQUEST)

        notify_email_validation(user)

        return Response({"details": "The email was sent"}, status=status.HTTP_200_OK)
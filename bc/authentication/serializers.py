from django.contrib.auth import authenticate
import os
from django.db.models import Q
from random import randint
from django.db import transaction
from django.utils.translation import ugettext_lazy as _

from rest_framework_jwt.settings import api_settings
from rest_framework_jwt.serializers import JSONWebTokenSerializer
from rest_framework import serializers

from jwt.exceptions import DecodeError

from .models import Device, User
from bc.utils import notifier

jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
jwt_decode_handler = api_settings.JWT_DECODE_HANDLER

"""
DEPENDANT SERIALIZERS
"""
class UserGetTinySerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')


class UserGetSmallSerializer(serializers.ModelSerializer):
    # profile = ProfileGetSmallSerializer(many=False)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')


class UserGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'first_name',
                  'last_name', 'email')





"""
MAIN SERIALIZERS
"""



class UserLoginSerializer(serializers.ModelSerializer):
    token = serializers.CharField(read_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password',
                  'token')
        extra_kwargs = {"password": {"write_only": True}}


class CustomJWTSerializer(JSONWebTokenSerializer):
    username_field = 'username_or_email'
    user = UserLoginSerializer(required=False)
    registration_id = serializers.CharField(write_only=True, required=False)
    exp_days = serializers.IntegerField(write_only=True, required=False)

    def validate(self, attrs):
        lookup = Q(email=attrs.get("username_or_email")) \
                 | Q(username=attrs.get("username_or_email"))

        password = attrs.get("password")
        user_obj = User.objects.filter(lookup).first()

        if not user_obj:
            msg = 'Account with this credentials does not exists'
            raise serializers.ValidationError(msg)

        if not user_obj.is_active:
            msg = _('User account is disabled. Have you confirmed your email?')
            raise serializers.ValidationError(msg)

        credentials = {
            'username': user_obj.username,
            'password': password
        }

        user = authenticate(**credentials)

        if not user:
            msg = 'Unable to log in with provided credentials.'
            raise serializers.ValidationError(msg)

        payload = jwt_payload_handler(user=user)
        device_id = attrs.get("registration_id")

        if device_id is not None:
            with transaction.atomic():
                Device.objects.filter(registration_id=device_id).delete()
                device = Device(user=user, registration_id=device_id)
                device.save()

        return {
            'token': jwt_encode_handler(payload),
            'user': user
        }

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(required=False, write_only=True)
    username = serializers.CharField(required=False)
    email = serializers.EmailField(required=False)

    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'is_active',
                  'last_name', 'email', 'password')

    def validate(self, data):
        if 'email' in data:
            email = data["email"]
            user = User.objects.filter(email=email)
            if user.exists():
                raise ValidationError("This email is already in use.")
        elif 'username' in data:
            username = data["username"]
            user = User.objects.filter(username=username)
            if user.exists():
                raise ValidationError("This username is already in use.")
        return data

    def create(self, validated_data):
        user = super(UserSerializer, self).create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

class UserRegisterSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    
    email = serializers.EmailField(required=True)
    first_name = serializers.CharField(required=True, max_length=50)
    last_name = serializers.CharField(required=True, max_length=50)
    bio = serializers.CharField(required=False, max_length=250)
    password = serializers.CharField(required=True, max_length=14, write_only=True)

    def validate(self, data):

        user = User.objects.filter(email=data["email"]).first()
        if len(data["email"]) > 150:
            raise serializers.ValidationError(
                "You email cannot contain more than 150 characters")

        if len(data["password"]) < 8:
            raise serializers.ValidationError("Password must be at least 8 characters long")
        if data["password"].lower() == data["password"]:
            raise serializers.ValidationError("Password must contain at least one uppercase letter")

        if len(data["first_name"]) == 0 or len(data["last_name"]) == 0:
            raise serializers.ValidationError(
                "Your first and last names must not be empty")

        return data

    def create(self, validated_data):

        user = User.objects.filter(email=validated_data["email"]).first()
        if not user:
            user = User.objects.create(**{**validated_data, "username": validated_data["email"]})

        user.set_password(validated_data['password'])
        user.save()

        notifier.send_email("registration",user.email,data={})

        return user


class ChangePasswordSerializer(serializers.Serializer):
    token = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)
    repeat_password = serializers.CharField(required=True)

    def validate(self, data):
        try:
            payload = jwt_decode_handler(data["token"])
        except DecodeError:
            raise serializers.ValidationError("Invalid token")

        user = User.objects.filter(id=payload["user_id"]).first()
        if user is None:
            raise serializers.ValidationError("User does not exist.")

        if data['new_password'] != data['repeat_password']:
            raise serializers.ValidationError("Passwords don't match")

        return data

    def create(self, validated_data):
        try:
            payload = jwt_decode_handler(validated_data["token"])
        except DecodeError:
            raise serializers.ValidationError("Invalid token")

        user = User.objects.get(id=payload["user_id"])
        user.set_password(validated_data['new_password'])
        user.save()
        return user
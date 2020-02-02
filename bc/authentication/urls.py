from django.urls import include, path
from rest_framework_jwt.views import ObtainJSONWebToken
from .serializers import CustomJWTSerializer
from .views import (
    PasswordView, ValidateEmailView, UserView, UserRegisterView, ValidateSendEmailView
)

urlpatterns = [
    #
    # PUBLIC ENDPOINTS
    #
    path('login', ObtainJSONWebToken.as_view(serializer_class=CustomJWTSerializer)),
    path('user', include('django.contrib.auth.urls'), name="user-auth"),
    path('user/password/reset',PasswordView.as_view(), name="password-reset-email"),
    path('user/email/validate',ValidateEmailView.as_view(), name="validate-email"),
    path('user/email/validate/send/<str:email>', ValidateSendEmailView.as_view(), name="validate-email-send"),
    path('user/<int:id>', UserView.as_view(), name="id-user"),
    path('user/register', UserRegisterView.as_view(), name="register")
]
from .serializers import UserSerializer
import datetime
from calendar import timegm
from rest_framework_jwt.settings import api_settings
from rest_framework.exceptions import APIException
from .models import User
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

def jwt_response_payload_handler(token, user=None, request=None):
    return {
        'token': token,
        'user': UserSerializer(
            user,
            context={
                'request': request}).data}


def internal_payload_encode(payload, exp_min=15):

    payload['exp'] = datetime.datetime.utcnow() + datetime.timedelta(seconds=(60 * exp_min)) # 15 min

    # Include original issued at time for a brand new token,
    # to allow token refresh
    if api_settings.JWT_ALLOW_REFRESH:
        payload['orig_iat'] = timegm(
            datetime.datetime.utcnow().utctimetuple()
        )

    if api_settings.JWT_AUDIENCE is not None:
        payload['aud'] = api_settings.JWT_AUDIENCE

    if api_settings.JWT_ISSUER is not None:
        payload['iss'] = api_settings.JWT_ISSUER

    # get user email to generate token
    email = None
    if 'user_email' in payload:
        email = payload['user_email']
    elif 'user_id' in payload:
        user = User.objects.get(id=payload['user_id'])
        email = user.email
    else:
        raise APIException("User email or id has to be specified on the token payload")

    token = jwt_encode_handler(payload)
    user_token = UserToken(token=token, email=email, expires_at=datetime.datetime.fromtimestamp(payload['exp'] / 1e3))
    user_token.save()

    return token
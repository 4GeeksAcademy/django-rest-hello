
1. Install django-oauth-toolkit
```
$ pip install django-oauth-toolkit
```

2. You need to ave at least these apps on settings.py

```
INSTALLED_APPS = (
    'django.contrib.admin',
    ...
    'oauth2_provider',
    'rest_framework',
)
```
3. Add the autentication class to the REST_FRAMEWORK

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'oauth2_provider.contrib.rest_framework.OAuth2Authentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    )
}

OAUTH2_PROVIDER = {
    # this is the list of available scopes
    'SCOPES': {'read': 'Read scope', 'write': 'Write scope', 'groups': 'Access to your groups'}
}

4. Import the classes on your views and use them as you wish.

from oauth2_provider.contrib.rest_framework import TokenHasReadWriteScope, TokenHasScope


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
    )
}

4.

from oauth2_provider.contrib.rest_framework import TokenHasReadWriteScope, TokenHasScope

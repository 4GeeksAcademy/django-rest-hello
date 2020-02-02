from rest_framework.views import exception_handler
from rest_framework.exceptions import ErrorDetail
from .notifier import get_template_content
from django.http import HttpResponse

def in_choices(choice, CHOICES):
    is_present = False
    for status, description in CHOICES:
        if description == choice:
            is_present = True
    return is_present

def error_object(msg, data=None):
    return {
        "details": msg
    }

def html_error(msg, data=None):
    template = get_template_content('general', {
        "status": "error",
        "msg": msg
    })
    return HttpResponse(template['html'], status=400)


def post_exception_handler(exc, context):
    # This is to be used with the Django REST Framework (DRF) as its
    # global exception handler.  It replaces the POST data of the Django
    # request with the parsed data from the DRF.  This is necessary
    # because we cannot read the request data/stream more than once.
    # This will allow us to see the parsed POST params in the rollbar
    # exception log.

    # Call REST framework's default exception handler first,
    # to get the standard error response.
    context['request']._request.POST = context['request'].data
    response = exception_handler(exc, context)

    # Now add the HTTP status code to the response.

    if response is not None:
        if isinstance(response.data, list):
            if response.data[0].code != 'invalid':
                response.data = { 'status_code': response.data[0].code, 'details': str(response.data[0]) }
            else:
                response.data = { 'status_code': 500, 'details': str(response.data[0]) }
        else:
            response.data['status_code'] = response.status_code

    return response
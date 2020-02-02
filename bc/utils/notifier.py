import os, requests
from django.core.mail import EmailMultiAlternatives
from rest_framework.exceptions import APIException
from django.template.loader import get_template
from django.template import Context
from django.conf import settings
from twilio.rest import Client

def send_email(slug, to, data={}):
    if settings.BREATHECODE_SETTINGS['EMAIL_NOTIFICATIONS']:
        template = get_template_content(slug, data, ["email"])
        # print('Email notification '+slug+' sent')
        return requests.post(
            "https://api.mailgun.net/v3/mailgun.breathecode.co/messages",
            auth=(
                "api",
                os.environ.get('MAILGUN_API_KEY')),
            data={
                "from": os.environ.get('MAILGUN_FROM') +
                " <mailgun@mailgun.jobcore.co>",
                "to": to,
                "subject": template['subject'],
                "text": template['text'],
                "html": template['html']}).status_code == 200
    else:
        # print('Email not sent because notifications are not enabled')
        return True

def send_sms(slug, phone_number, data={}):

    template = get_template_content(slug, data, ["sms"])
    # Your Account Sid and Auth Token from twilio.com/console
    # DANGER! This is insecure. See http://twil.io/secure
    TWILLIO_SID = os.environ.get('TWILLIO_SID')
    TWILLIO_SECRET = os.environ.get('TWILLIO_SECRET')
    client = Client(TWILLIO_SID, TWILLIO_SECRET)

    try:
        message = client.messages.create(
            body=template['sms'],
            from_='+15017122661',
            to='+1'+phone_number
        )
        return True
    except Exception:
        return False


def send_mobile_notification(slug, registration_ids, data={}):
    if(len(registration_ids) > 0 and push_service):
        template = get_template_content(slug, data, ["email", "mobile"])

        if 'mobile' not in template:
            raise APIException(
                "The template " +
                slug +
                " does not seem to have a valid mobile notification version")

        message_title = template['subject']
        message_body = template['message']
        if 'DATA' not in data:
            raise Exception("There is no data for the notification")
        message_data = data['DATA']

        result = push_service.notify_multiple_devices(
            registration_ids=registration_ids,
            message_title=message_title,
            message_body=message_body,
            data_message=message_data)

        return result
    else:
        return False


def send_fcm_notification(slug, device_set=[], data={}):
    registration_ids = [device.registration_id for device in device_set]
    send_fcm(slug, registration_ids, data)


def get_template_content(slug, data={}, formats=[]):
    templates = []
    if "email" in formats:
        plaintext = get_template(slug + '.txt')
        html = get_template(slug + '.html')
        templates["text"] = plaintext.render(data)
        templates["html"] = html.render(data)

    if "mobile" in formats:
        fms = get_template(slug + '.mobile')
        templates["mobile"] = fms.render(data)

    if "sms" in formats:
        sms = get_template(slug + '.sms')
        templates["sms"] = sms.render(data)

    return templates
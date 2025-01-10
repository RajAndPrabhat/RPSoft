from django.conf import settings
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core.mail import send_mail
from background_task import background

class EmailService():
    @background(schedule=10)
    def enquiryEmail(request):
        address = request['to']
        subject = request['subject']
        message = request['message']
        template = request['template']
        
        html_message = render_to_string(template, message)    
        plain_message = strip_tags(html_message)    
        try:
            send_mail(subject, plain_message, settings.EMAIL_HOST_USER, [address])
            return True
        except Exception as e:
            print(f'Error sending Email :: {e}')
            return False

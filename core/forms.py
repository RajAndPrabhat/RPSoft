from django import forms
from django_recaptcha.fields import ReCaptchaField
from django_recaptcha.widgets import ReCaptchaV3

class EnquiryForm(forms.Form):
    first_name=forms.CharField(label="First Name", help_text="First Name")
    last_name=forms.CharField(label="Last Name", help_text="Last Name")
    email=forms.CharField(label="Email ID", help_text="Email ID")
    phone=forms.CharField(label="Phone No", help_text="Phone Number")
    subject=forms.CharField(help_text="Subject")
    message=forms.CharField(widget=forms.Textarea(), help_text="Leave your message")
    captcha = ReCaptchaField(widget=ReCaptchaV3) 




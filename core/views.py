from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import EnquiryForm
from dotenv import load_dotenv
import os
from .email_service import EmailService
from .models import Testimonial, Service, Slider, TeamMember, Client, Portfolio, Lead
from django.shortcuts import redirect
from django.contrib import messages


load_dotenv()

# Create your views here.
def home(request):    
    file_path="core/pages/home.html"
    sliders=Slider.objects.all().order_by('-id')
    testimonials=Testimonial.objects.all().order_by('-id')
    services=Service.objects.all().order_by('-id')
    team_members=TeamMember.objects.all().order_by('-id')
    clients=Client.objects.all().order_by('-id')
    portfolios=Portfolio.objects.all().order_by('-id')[:6]
    form=EnquiryForm()
    context={
        'title':'Home',
        'sliders':sliders,
        'testimonials':testimonials,
        'services':services,
        'team_members':team_members,
        'clients':clients,
        'portfolios':portfolios,
        'form':form
    }
    return render(request, file_path, context)


def about(request):
    file_path="core/pages/about.html"
    team_members=TeamMember.objects.all().order_by('-id')
    clients=Client.objects.all().order_by('-id')
    context={
        'title':'About Us',
        'team_members':team_members,
        'clients':clients
    }
    return render(request, file_path, context)

def contact(request):
    file_path="core/pages/contact.html"
    clients=Client.objects.all().order_by('-id')
    form=EnquiryForm()
    context={
        'title':'Contact Us',
        'clients':clients,
        'form':form
    }
    return render(request, file_path, context)

def services(request):
    file_path="core/pages/services.html"
    testimonials=Testimonial.objects.all().order_by('-id')
    services=Service.objects.all().order_by('-id')
    clients=Client.objects.all().order_by('-id')
    context={
        'title':'Services',
        'testimonials':testimonials,
        'services':services,
        'clients':clients
    }
    return render(request, file_path, context)

def portfolio(request):
    file_path="core/pages/portfolio.html"
    testimonials=Testimonial.objects.all()
    portfolios=Portfolio.objects.all()
    clients=Client.objects.all()
    context={
        'title':'Services',
        'testimonials':testimonials,
        'portfolios':portfolios,
        'clients':clients
    }
    return render(request, file_path, context)

def enquiry(request):
    if request.method=="POST":
        enquiry_form=EnquiryForm(request.POST)
        if enquiry_form.is_valid():
            cleaned_data=enquiry_form.cleaned_data

            lead = Lead() 
            lead.first_name = cleaned_data['first_name']
            lead.last_name = cleaned_data['last_name']
            lead.email = cleaned_data['email']
            lead.phone = cleaned_data['phone']
            lead.subject = cleaned_data['subject']
            lead.message = cleaned_data['message']
            lead.save()   

            mail_message={
                'to':os.getenv("LEAD_ADMIN_EMAIL_ID"),  
                'subject':'New Lead for '+os.getenv("APP_NAME"),  
                'template':'core/mail/enquiry_mail.html',  
                'message':{
                    'name':cleaned_data['first_name']+" "+cleaned_data['last_name'],
                    'email':cleaned_data['email'],
                    'phone':cleaned_data['phone'],
                    'subject':cleaned_data['subject'],
                    'message':cleaned_data['message']
                },  
            }
            email_obj=EmailService()
            mail_status=email_obj.enquiryEmail(mail_message)
            messages.success(request, 'Form submission successful')
            return redirect(request.META.get('HTTP_REFERER'))
    else:
        pass
    return True
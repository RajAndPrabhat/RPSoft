from django.shortcuts import render
from django.http import HttpResponse
from .models import Testimonial, Service, Slider, TeamMember, Client, Portfolio

# Create your views here.
def home(request):
    file_path="core/pages/home.html"
    sliders=Slider.objects.all()
    testimonials=Testimonial.objects.all()
    services=Service.objects.all()
    team_members=TeamMember.objects.all()
    clients=Client.objects.all()
    portfolios=Portfolio.objects.all()
    context={
        'title':'Home',
        'sliders':sliders,
        'testimonials':testimonials,
        'services':services,
        'team_members':team_members,
        'clients':clients,
        'portfolios':portfolios
    }
    return render(request, file_path, context)


def about(request):
    file_path="core/pages/about.html"
    team_members=TeamMember.objects.all()
    clients=Client.objects.all()
    context={
        'title':'About Us',
        'team_members':team_members,
        'clients':clients
    }
    return render(request, file_path, context)

def contact(request):
    file_path="core/pages/contact.html"
    clients=Client.objects.all()
    context={
        'title':'Contact Us',
        'clients':clients
    }
    return render(request, file_path, context)

def services(request):
    file_path="core/pages/services.html"
    testimonials=Testimonial.objects.all()
    services=Service.objects.all()
    context={
        'title':'Services',
        'testimonials':testimonials,
        'services':services
    }
    return render(request, file_path, context)
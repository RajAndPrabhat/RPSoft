from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    file_path="core/pages/home.html"
    context={
        'title':'Home'
    }
    return render(request, file_path, context)


def about(request):
    file_path="core/pages/about.html"
    context={
        'title':'About Us'
    }
    return render(request, file_path, context)

def contact(request):
    file_path="core/pages/contact.html"
    context={
        'title':'Contact Us'
    }
    return render(request, file_path, context)
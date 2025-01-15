from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField 

# Create your models here.
class Service(models.Model):
    name=models.CharField(max_length=200)
    description=models.TextField(max_length=500)
    service_icon=models.CharField(max_length=200)

class Testimonial(models.Model):
    name=models.CharField(max_length=200)
    description=RichTextUploadingField()
    designation=models.CharField(max_length=100, null=True)
    image_file=models.ImageField(upload_to='testimonial')
    

class Slider(models.Model):
    heading=models.CharField(max_length=200)
    description=models.TextField(max_length=500)
    image_file=models.ImageField(upload_to='sliders')

class TeamMember(models.Model):
    name=models.CharField(max_length=200)
    designation=models.CharField(max_length=50, null=True, default='')
    twitter_url=models.URLField(null=True, default='')
    linkedin_url=models.URLField(null=True, default='')
    facebook_url=models.URLField(null=True, default='')
    instgram_url=models.URLField(null=True, default='')
    image_file=models.ImageField(upload_to='teams')


class Client(models.Model):
    name=models.CharField(max_length=200)
    image_file=models.ImageField(upload_to='clients')

class Portfolio(models.Model):
    name=models.CharField(max_length=200)
    link_url=models.URLField(null=True, default='')
    image_file=models.ImageField(upload_to='portfolios')

class Lead(models.Model):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    email=models.CharField(max_length=200)
    phone=models.CharField(max_length=20)
    subject=models.CharField(max_length=50)
    message=models.TextField()
    created_at=models.DateTimeField(auto_now=True)
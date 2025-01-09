from django.contrib import admin
from .models import Service, Testimonial, Slider, TeamMember, Client, Portfolio
from django.utils.html import format_html

# Register your models here.
@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display=[field.name for field in Service._meta.get_fields()]
    list_filter = ["name"]

@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    def image_tag(self, obj):
        return format_html('<img src="{}" height="50px" />'.format(obj.image_file.url))
    image_tag.short_description = 'Image File'

    list_display=['id','image_tag','name','designation','description']
    list_filter = ["name","designation"]

@admin.register(Slider)
class SliderAdmin(admin.ModelAdmin):
    def image_tag(self, obj):
        return format_html('<img src="{}" height="50px" />'.format(obj.image_file.url))
    image_tag.short_description = 'Image File'

    list_display=['id','image_tag','heading','description']
    list_filter = ["heading"]

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    def image_tag(self, obj):
        return format_html('<img src="{}" height="50px" />'.format(obj.image_file.url))
    image_tag.short_description = 'Image File'

    list_display=['id','image_tag','name']
    list_filter = ["name"]


@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    def image_tag(self, obj):
        return format_html('<img src="{}" height="50px" />'.format(obj.image_file.url))
    image_tag.short_description = 'Image File'

    list_display=['id','image_tag','name','designation','twitter_url','linkedin_url','facebook_url','instgram_url']
    list_filter = ["name",'designation']



@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    def image_tag(self, obj):
        return format_html('<img src="{}" height="50px" />'.format(obj.image_file.url))
    image_tag.short_description = 'Image File'

    list_display=['id','image_tag','name','link_url']
    list_filter = ["name"]

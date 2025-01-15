"""
URL configuration for rpsoft project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from dotenv import load_dotenv
import os
load_dotenv()


admin.site.site_title = os.getenv("ADMIN_SITE_TITLE")
admin.site.site_header =os.getenv("ADMIN_SITE_HEADER")
admin.site.index_title = os.getenv("ADMIN_SITE_INDEX_TITLE")
admin.site.site_url = "/"
admin.site.enable_nav_sidebar = True
admin.site.empty_value_display = "-"




urlpatterns = [
    path('', include('core.urls')),
    path('admin/', admin.site.urls),
    re_path(r'^ckeditor/', include('ckeditor_uploader.urls')), # The CKEditor path
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

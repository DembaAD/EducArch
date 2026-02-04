"""EducArch URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.conf import settings  
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
#from django.conf.urls import url
from django.conf.urls.static import static
from django.shortcuts import render
from django.contrib import *
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.base import TemplateView
from django.views.static import serve


urlpatterns = [

	path('site/', include('archblog.urls')),
    path('',TemplateView.as_view(template_name='archblog/home.html'), name='home'),
    path('accounts/', include('django.contrib.auth.urls')),
    # path('accounts/logout', registration),
    # path('accounts/signup/', SignUpView.as_view(), name='signup'),
    # path('accounts/signup/student/', StudentSignUpView.as_view(), name='student_signup'),
    # path('accounts/signup/teacher/', TeacherSignUpView.as_view(), name='teacher_signup'),

    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT, show_indexes=True)
if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        re_path(r'^__debug__/', include(debug_toolbar.urls)),
        ] + urlpatterns

# urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
# urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

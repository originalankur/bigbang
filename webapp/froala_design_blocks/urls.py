"""app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import include, path
from froala_design_blocks import views

urlpatterns = [
    path('', views.home, name='home'),
    path('call-to-action/', views.call_to_action, name='call_to_action'),
    path('contacts/', views.contacts, name='contacts'),
    path('contents/', views.contents, name='contents'),
    path('features/', views.features, name='features'),
    path('footers/', views.footers, name='footers'),
    path('forms/', views.forms, name='forms'),
    path('headers/', views.headers, name='headers'),
    path('pricings/', views.pricings, name='pricings'),
    path('teams/', views.teams, name='teams'),
    path('testimonials/', views.testimonials, name='testimonials')
]
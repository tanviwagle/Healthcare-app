"""Health_App URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path
from Health_App import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('admin/', admin.site.urls),
    path('heart_pred', views.heart_pred, name='heart'),
    path('liver_pred', views.liver_pred, name='liver'),
    path('stroke_pred', views.stroke_pred, name='stroke'),
    path('heart_disease_result', views.heart_disease_result, name='heart_disease_result'),
    path('brain_stroke_result', views.brain_stroke_result, name='brain_stroke_result'),
    path('liver_disease_result', views.liver_disease_result, name='liver_disease_result'),
    path('heart_remedies', views.heart_remedies, name='heart_remedies'),
    path('liver_remedies', views.liver_remedies, name='liver_remedies'),
    path('brain_remedies', views.brain_remedies, name='brain_remedies'),
]

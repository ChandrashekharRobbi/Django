# revear_app url
from django.contrib import admin
from django.urls import path, include
from django.shortcuts import HttpResponse
from . import views

urlpatterns = [
    path('',views.greet),
    path('submitParser/', views.submit),
    path('all/', views.all),
    path('bt', views.Bt),
]

from django.urls import path, include
from django.http import HttpResponse
from . import views

urlpatterns = [
    path('', views.home,name='home'),
    path('room_pages/<str:id>', views.room, name='room'),
    path('room_form/',views.room_form, name="room_form"),
    path('update_form/<str:id>/',views.updateForm, name="update_form"),
    path('delete_form/<str:id>/',views.deleteForm, name="delete_form"),
]
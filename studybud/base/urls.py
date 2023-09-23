from . import views
from django.http import HttpResponse
from django.urls import path, include

urlpatterns = [
    path('', views.home,name='home'),
    path('login/', views.loginPage,name='login'),
    path('register/', views.registerPage,name='register'),
    path('logout/', views.logoutUser,name='logout'),
    path('room_pages/<str:id>', views.room, name='room'),
    path('room_form/',views.room_form, name="room_form"),
    path('update_form/<str:id>/',views.updateForm, name="update_form"),
    path('delete_form/<str:id>/',views.deleteForm, name="delete_form"),
]
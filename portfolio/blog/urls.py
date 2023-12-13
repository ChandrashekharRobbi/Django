from django.contrib import admin
from django.urls import path, include
from . import views
admin.site.site_header = 'CR admin'
admin.site.site_title = 'Chandrashekhar admin'
admin.site.site_header = 'Welcome to Chandrashekhar admin'
admin.site.index_title = 'Welcome to this portal'
admin.site.site_url = 'https://chandrashekharrobbi.github.io/Website/'
admin.empty_value_display = '**Empty**'

urlpatterns = [
    path('', views.Greeting),
    path('home/', views.Home),
    path('about', views.About),
    path('contact', views.Contact, name='contact'),
    path('bootstrap', views.Bootstrap),
    path('profiles', views.Profiles),
    path('urlTest/', views.urlDispatcher)
]

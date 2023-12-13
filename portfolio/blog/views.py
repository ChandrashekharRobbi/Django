from django.shortcuts import render, HttpResponse, redirect
from blog import models
# Create your views here.
def Greeting(request):
    return HttpResponse("Hello There :)")

def Home(request):
    context = {'name' : 'Chandrashekhar', 'LastName':'Robbi', 'Experience' : 3}
    return render(request, 'home.html', context)

def About(request):
    return render(request, 'about.html')

def Contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        phone = request.POST['phone']
        email = request.POST['email']
        desc = request.POST['desc']
        contact_instance = models.Contact(name=name, phone=phone, email=email, desc=desc)
        contact_instance.save()
         
    return render(request, 'contact.html')

def Profiles(request):
    return render(request, 'profiles.html')

def urlDispatcher(request):
    test = request.GET.get('test')
    return HttpResponse(f"A Test To URL Dispatcher <br>test : {test}")

def Bootstrap(request):
    return render(request, 'bootstrap.html')
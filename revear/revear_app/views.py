from django.shortcuts import render, HttpResponse, redirect
from . import models
from django.utils import timezone
from datetime import date, timedelta

# Create your views here.
def greet(request):
    value = models.TaskData.objects.all()
    curr_date = timezone.now().date()
    submit = False
    for each in value:
        date_count = each.datebetween.days
        if date_count == 1 or date_count == 3 or (date_count > 1 and date_count % 7 == 0):
            submit = True
        else:
            submit = False
    show = False
    context = {'value' : value, 'curr_date' : curr_date, 'submit': submit}
    return render(request, 'index.html', context)

def all(request):
    value = models.TaskData.objects.all()
    context = {
        "value" : value
    }
    return render(request, 'taskList.html', context)

def submit(request):
    if request.method == 'POST':
        name = request.POST['text']
        rowInstance = models.TaskData(name=name)
        rowInstance.save()
    return render(request, 'submit.html')
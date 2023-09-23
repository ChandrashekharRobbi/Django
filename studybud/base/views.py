from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.db.models import Q
from .models import Rooms, Topic
from .forms import RoomForm

# Create your views here.
def home(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    # it will filter based on the topic name
    room = Rooms.objects.filter(
        Q(topic__name__icontains=q) |
        Q(name__icontains=q) |
        Q(description__icontains=q) |
        Q(host__username__icontains=q)
        )
    room_count = room.count()
    topics = Topic.objects.all()
    context = {'val': room, 'topics': topics, 'room_count': room_count}
    return render(request, 'base/home.html', context)


def room(request,id):
    room = Rooms.objects.get(id=id)
    context = {
        'room': room
    }
    return render(request, 'base/room.html', context)

def room_form(request):
    # fetching empty form
    form = RoomForm()
    if request.method == 'POST':
        # filling the details in the form
        form = RoomForm(request.POST)
        # checking if the form is valid
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {
        'form': form
    }
    return render(request, 'base/room_form.html', context)

def updateForm(request, id):
    # fetching the room details for the given id
    room = Rooms.objects.get(id = id)
    # filling the form with the room details of given id
    form = RoomForm(instance=room)
    if request.method == 'POST':
        # updating the form with the new details on the same instance
        form = RoomForm(request.POST, instance=room)
        # checking if the form is valid
        if form.is_valid():
            # saving the form
            form.save()
            # redirecting to home page
            return redirect('home')
    context = {'form': form}
    return render(request, 'base/room_form.html', context)

def deleteForm(request, id):
    room = Rooms.objects.get(id=id)
    if request.method == 'POST':
        room.delete()
        return redirect('home')
    context = {'room': room}
    return render(request, 'base/delete_form.html', context)



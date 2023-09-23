from .forms import RoomForm
from django.db.models import Q
from .models import Rooms, Topic
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout

# Create your views here.


def loginPage(request):
    """
    Renders the login page and authenticates user credentials.

    If the request method is POST, the function attempts to authenticate the user's
    credentials. If the user is authenticated, the function logs the user in and redirects
    them to the home page. If the user is not authenticated, an error message is displayed.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The HTTP response object containing the rendered login page.
    """

    # if the user is already logged in then it will redirect to home page
    if request.user.is_authenticated:
        return redirect("home")
    
    page = 'login'

    if request.method == "POST":
        username = request.POST.get("username").lower()
        password = request.POST.get("password")

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, "Username does not exist")
        # checking user is authenticated or not
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            messages.error(request, "Username or Password is incorrect")

    context = {'page': page}
    return render(request, "base/login_register.html", context)


def logoutUser(request):
    """
    Logs out the user and redirects to the home page.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponseRedirect: A redirect to the home page.
    """
    logout(request)
    return redirect("home")

def registerPage(request):
    form = UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        # checking if the form is valid
        if form.is_valid():
            # saving the form
            user = form.save(commit=False)
            # fetching the username
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect("home")
        else:
            messages.error(request, "An error occured during registration")
    context = {"form": form}
    return render(request, 'base/login_register.html', context)

def home(request):
    """
    This view function handles the rendering of the home page of the website.
    It takes a GET request and filters the Rooms objects based on the query parameter 'q'.
    The filtering is done based on the topic name, room name, description and host username.
    It also retrieves all the Topic objects and passes them to the context.
    Finally, it renders the 'base/home.html' template with the filtered rooms, topics and room count.
    """
    q = request.GET.get("q") if request.GET.get("q") != None else ""
    # it will filter based on the topic name
    room = Rooms.objects.filter(
        Q(topic__name__icontains=q)
        | Q(name__icontains=q)
        | Q(description__icontains=q)
        | Q(host__username__icontains=q)
    )
    room_count = room.count()
    topics = Topic.objects.all()
    context = {"val": room, "topics": topics, "room_count": room_count}
    return render(request, "base/home.html", context)


def room(request, id):
    """
    This function takes a request and an id as input parameters and returns a rendered HTML page with the details of a room.

    Args:
        request: A HttpRequest object that contains metadata about the current request.
        id: An integer representing the id of the room to be displayed.

    Returns:
        A rendered HTML page with the details of the specified room.
    """
    room = Rooms.objects.get(id=id)
    context = {"room": room}
    return render(request, "base/room.html", context)


# this decorator will handle if the user is logged in or not
# if not then it will redirect to login page
@login_required(login_url="login")
def room_form(request):
    """
    This view handles the creation of a new room by rendering a form and saving the data submitted by the user.
    If the user is not authenticated, they will be redirected to the login page.
    """
    # fetching empty form
    form = RoomForm()
    if request.method == "POST":
        # filling the details in the form
        form = RoomForm(request.POST)
        # checking if the form is valid
        if form.is_valid():
            form.save()
            return redirect("home")
    context = {"form": form}
    return render(request, "base/room_form.html", context)


@login_required(login_url="login")
def updateForm(request, id):
    # fetching the room details for the given id
    room = Rooms.objects.get(id=id)
    # filling the form with the room details of given id
    form = RoomForm(instance=room)

    if request.user != room.host:
        return HttpResponse(f"You are not allowed to edit this room which was originally created by {room.host.username}")
    

    if request.method == "POST":
        # updating the form with the new details on the same instance
        form = RoomForm(request.POST, instance=room)
        # checking if the form is valid
        if form.is_valid():
            # saving the form
            form.save()
            # redirecting to home page
            return redirect("home")
    context = {"form": form}
    return render(request, "base/room_form.html", context)


@login_required(login_url="login")
def deleteForm(request, id):
    room = Rooms.objects.get(id=id)

    if request.user != room.host:
        return HttpResponse(f"You are not allowed to delete this room which was originally created by {room.host.username}")
    
    if request.method == "POST":
        room.delete()
        return redirect("home")
    context = {"room": room}
    return render(request, "base/delete_form.html", context)

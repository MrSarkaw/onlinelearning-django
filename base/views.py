from django.shortcuts import redirect, render
from .models import Room, Topic
from .forms import RoomForm
from django.contrib import messages
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

def home(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''

    rooms = Room.objects.filter(Q(topic__name__icontains = q) | Q(name__icontains = q))
    topic = Topic.objects.all()

    return render(request, 'base/home.html', {'content':rooms, 'topic':topic})

def loginPage(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            user = User.objects.get(username = username)
        except:
            messages.error(request, "user not found, if you not register yet, regitster!")
        
        user = authenticate(request,username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'username or email is wrong')

    return render(request,'base/login_register.html', {'name':'login'})

def registerPage(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
        else:
            messages.error(request,'an error accured, tryagain')
    return render(request, 'base/login_register.html',{'form':UserCreationForm()})

def room(request, id):
    room = Room.objects.get(id = int(id))
    
    return render(request, 'base/room.html',{"room":room})

@login_required(login_url='loginPage')
def logoutPage(request):
    logout(request)
    return redirect('home')

@login_required(login_url='loginPage')
def roomCreate(request):
    if request.method == "POST":
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
    return render(request,'base/roomCreate.html',{'form': RoomForm})

@login_required(login_url='loginPage')
def roomUpdate(request,pk):
    room = Room.objects.get(id=int(pk))
    form = RoomForm(instance=room)

    if request.method == 'POST':
        form = RoomForm(request.POST, instance=room)
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(request,'base/roomCreate.html',{'form': form})

@login_required(login_url='loginPage')
def deleteRoom(request, pk):
    room = Room.objects.get(id=int(pk))
    
    if request.method == "POST":
        room.delete()
        return redirect("home")
    return render(request,'base/delete.html',{'obj': room})

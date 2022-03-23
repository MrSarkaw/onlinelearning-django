from django.shortcuts import redirect, render
from .models import Room, Topic
from .forms import RoomForm
from django.contrib import messages
from django.db.models import Q
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate


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

            user = authenticate(request,username=username, password=password)
            print(user)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.error(request, 'username or email is wrong')
        except:
            messages.error(request, "user not found, if you not register yet, regitster!")
        

    return render(request,'base/login_register.html',{"name":'login'})

def registerPage(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            print('hello')
            user = form.save()
            login(request, user)
            return redirect('home')

    return render(request, 'base/login_register.html',{'form':UserCreationForm})



def room(request, id):
    room = Room.objects.get(id = int(id))
    
    return render(request, 'base/room.html',{"room":room})

def logoutPage(request):
    logout(request)
    return redirect('home')

def roomCreate(request):
    if request.method == "POST":
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
    return render(request,'base/roomCreate.html',{'form': RoomForm})

def roomUpdate(request,pk):
    room = Room.objects.get(id=int(pk))
    form = RoomForm(instance=room)

    if request.method == 'POST':
        form = RoomForm(request.POST, instance=room)
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(request,'base/roomCreate.html',{'form': form})

def deleteRoom(request, pk):
    room = Room.objects.get(id=int(pk))
    
    if request.method == "POST":
        room.delete()
        return redirect("home")
    return render(request,'base/delete.html',{'obj': room})

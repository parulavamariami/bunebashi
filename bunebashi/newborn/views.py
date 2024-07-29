from django.shortcuts import render, redirect
from .models import Service, User, Type
from django.db.models import Q
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
#from forms import MyUserCreationForm, BookForm, UserForm

def home(request):
    return render(request, 'newborn/home.html')

def about(request):
    heading = 'What About Us?'
    context = {'heading': heading}
    return render(request, 'newborn/about.html', context)

def contact(request):
    heading = 'Contact Info'
    context = {'heading': heading}
    return render(request, 'newborn/contact.html', context)
def sservices(request):
    lookfor = request.GET.get("lookfor") if request.GET.get("lookfor") is not None else ''
    services = Service.objects.filter(Q(title__icontains=lookfor) | Q(type__name__icontains=lookfor))
    services = list(set(services))
    heading = 'Services'
    type = Type.objects.all()
    context = {'services': services, 'heading': heading, 'type': type}
    return render(request, 'newborn/services.html', context)
@login_required(login_url='login')
def profile(request, userid):
    user = User.objects.get(id=userid)
    services = user.services.all()
    heading = 'My Wishlist'
    context = {'services': services, 'heading': heading}
    return render(request, 'newborn/profile.html', context)
@login_required(login_url='login')
def saving(request, userid):
    user = request.user
    serviceid = Service.objects.get(id=userid)
    user.services.add(serviceid)
    return redirect('profile', user.id)
@login_required(login_url='login')
def remove(request, userid):

    obj = Service.objects.get(id=userid)
    heading = f'Are you sure you want to remove {obj}?'
    context = {'heading': heading, 'obj': obj}

    if request.method == "POST":
        request.user.services.remove(obj)
        return redirect('profile', request.user.id)

    return render(request, 'newborn/delete.html', context)

def login_user(request):

    if request.user.is_authenticated:
        return redirect('newborn/profile.html', request.user.id)

    if request.method == 'POST':
        username = request.POST.get('username').lower()
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
        except:
            pass

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('profile', request.user.id)
        else:
            pass

    heading = 'Log in'
    context = {'heading': heading}
    return render(request, 'newborn/login.html', context)

def logout_user(request):
    logout(request)
    return redirect('home')

def register_user(request):

    heading = 'Sign Up'
    context = {'heading': heading} #'form': form}
    return render(request, 'newborn/register.html', context)
''' 
    
    form = MyUserCreationForm()

    if request.method == 'POST':
        form = MyUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('profile', user.id)
        else:
            pass'''




"""def myservices(request, userid):
    registred_users = Service.user.all()
    print(registred_users)

    return render(request, 'newborn/my_services.html', context)"""
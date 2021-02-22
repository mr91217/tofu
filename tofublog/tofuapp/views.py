from django.shortcuts import render
from tofuapp.models import UserProfileInfo
from tofuapp.forms import UserForm, UserProfileInfoForm
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def index(request):
    return render(request, 'tofuapp/index.html')



@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

def tofu(request):
    return render(request, 'tofuapp/tofu.html')

def lulu(request):
    return render(request, 'tofuapp/lulu.html')

def lucas(request):
    return render(request, 'tofuapp/lucas.html')

def aflogin(request):
    return render(request, 'tofuapp/aflogin.html')


def register(request):
    registered = False
    if request.method =="POST":
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.Files['profile_pic']

            profile.save()

            registered = True
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()

    return render(request, 'tofuapp/registration.html',{'user_form':user_form,'profile_form':profile_form,'registered':registered})

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('tofuapp:aflogin'))
            else:
                return HttpResponse("Account not active")
        else:
            print("some one try to login and failed")
            print("Username:{} and password:{}".format(username,password))
            return HttpResponse("invalid login")
    else:
        return render(request, 'tofuapp/login.html',{})

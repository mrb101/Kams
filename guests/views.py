from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout, login, authenticate
from forms import GuestProfileForm, GuestRegisterationForm


def list(request):
    pass


def login_view(request):
    template = 'guests/login.html'
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                messages.success(request, "You have successfully logged in!")
                return redirect('home')
            else:
                messages.warning(request, "Your account is disabled!")
                return redirect('/guests/login')
        else:
            messages.warning(request, "The username or password are not valid!")
            return redirect('/guests/login')
    context = {}
    return render(request, template, context)


@login_required(login_url='/guests/login')
def logout_view(request):
    logout(request)
    return redirect('home')


def register(request):
    template = 'guests/register.html'
    form = GuestRegisterationForm(request.POST or None)
    if form.is_valid:
        form.save()
        login(new_user)
        messages.success(request, "You are now registered!")
        return redirect('home')
    context = {}
    return render(request, template, context)




from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import SignUpForm

def home(request):
    return render(request, "home.html")
    
def registration(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "You successfully login.")
            return redirect("users:profile")
    else:
        form= SignUpForm()
    return render(request, "users/registration.html", {"form" : form})

@login_required
def profile(request):
    return render(request, "users/profile.html")

def custom_logout(request):
    if request.method == "POST":
        logout(request)
        messages.success(request, "You successfully logout.")
        return redirect("users:home")
    return redirect("users:login")
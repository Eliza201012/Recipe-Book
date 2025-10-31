from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .forms import SignUpForm, UpdateUserForm

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

@login_required
def update_profile(request):
    if request.method == "POST":
        user_form = UpdateUserForm(request.POST, instance=request.user)
        if user_form.is_valid():
            user_form.save()
            messages.success(request, "Your username and email is updated successfully.")
            return redirect("users:profile")
    else:
        user_form = UpdateUserForm(instance=request.user)
    return render(request, "users/update_profile_form.html", {"user_form" : user_form})
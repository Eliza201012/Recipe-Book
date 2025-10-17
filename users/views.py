from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import SignUpForm

def home(request):
    return render(request, "home.html")
    
def registration(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("users:profile")
    else:
        form= SignUpForm()
    return render(request, "users/registration.html", {"form" : form})

@login_required
def profile(request):
    return render(request, "users/profile.html")
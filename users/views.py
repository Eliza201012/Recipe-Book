from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import SignUpForm

def registration(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("users:profile")
        else:
            form= SignUpForm()
    return render(request, "user/registration.html", {"form" : form})

@login_required
def profile(request):
    return render(request, "user/profile.html")
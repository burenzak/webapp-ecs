from django.shortcuts import render, redirect
from django.http import HttpResponse
from datetime import datetime
from posts.models import Post
from .forms import UserRegisterForm
from django.contrib.auth import authenticate, login
from django.contrib import messages

# Create your views here.


def welcome(request):
    return render(request, "website/welcome.html",
                  {'current_time': datetime.now(),
                  "posts": Post.objects.all(),
                  "num_posts": Post.objects.count(),})


def signup(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            login(request, new_user)
            messages.success(request, f"Account created for {form.cleaned_data['username']}")
            return redirect('/')
    else:
        form = UserRegisterForm()
    return render(request, "registration/signup.html", {"form": form})


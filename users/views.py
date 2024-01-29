from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse

from users.forms import LoginForm


def user_login(request):
    if request.method == "POST":
        loginForm = LoginForm(request.POST)
        if loginForm.is_valid():
            data = loginForm.cleaned_data
            user = authenticate(
                request, username=data["username"], password=data["password"]
            )
            if user is not None:
                login(request, user)
                return redirect('index')
            else:
                return HttpResponse("Invalid Credentials")
    else:
        loginForm = LoginForm()
        return render(request, "users/login.html", {"form": loginForm})


def user_logout(request):
    logout(request)
    return render(request, "users/logout.html", {})

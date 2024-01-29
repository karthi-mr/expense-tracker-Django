from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.shortcuts import redirect, render

from users.forms import LoginForm, RegisterForm


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
                return render(
                    request,
                    "users/login.html",
                    {
                        "form": loginForm,
                        "error_message": "Invalid Credentials. Please try again.",
                    },
                )
    else:
        loginForm = LoginForm()
        return render(request, "users/login.html", {"form": loginForm})


def user_logout(request):
    logout(request)
    return render(request, "users/logout.html", {})


def user_register(request):
    if request.method == 'POST':
        registerForm = RegisterForm(request.POST)
        if registerForm.is_valid():
            newUser = registerForm.save(commit=False)
            newUser.set_password(registerForm.cleaned_data["password"])
            newUser.save()
            return render(request, "users/register_done.html", {})
    registerForm = RegisterForm()
    return render(request, "users/register.html", {"form": registerForm})

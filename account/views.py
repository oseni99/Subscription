from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login,logout

from .forms import CreateUserForm

def home_page(request):
    return render(request, "account/index.html")


def register(request):
    form = CreateUserForm()

    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("User Succesfully Registered")
    return render(request, "account/register.html", {
            "registered_form":form
        })

def my_login(request):
    form = AuthenticationForm()
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            if user is not None:
                login(request,user)
                if user.is_writer:
                    return redirect("writer-dashboard")
                else:
                    return redirect("client-dashboard")
    else:
        form = AuthenticationForm()
                
    return render(request, "account/login.html", {
        "login_form":form
        })

def user_logout(request):
    logout(request)
    return redirect("login")

import os

from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes, force_str
from dotenv import load_dotenv

from .forms import CreateUserForm
from .models import CustomUser
from .token import urlsafe_base64_decode, urlsafe_base64_encode, user_tokenize_generator

load_dotenv()


def home_page(request):
    return render(request, "account/index.html")


def register(request):
    form = CreateUserForm()

    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            email_user_host = os.getenv("EMAIL_HOST_USER")
            subject = "Activate your account"
            message = render_to_string(
                "account/email-verification.html",
                {
                    "user": user,
                    "current_site": current_site.domain,
                    "uid": urlsafe_base64_encode(force_bytes(user.pk)),
                    "token": user_tokenize_generator.make_token(user),
                },
            )
            user_email = user.email
            send_mail(
                subject=subject,
                message=message,
                from_email=email_user_host,
                recipient_list=[user_email],
            )
            return redirect("email_verification_sent")
    return render(request, "account/register.html", {"registered_form": form})


def my_login(request):
    form = AuthenticationForm()
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            if user is not None:
                login(request, user)
                if user.is_writer:
                    return redirect("writer-dashboard")
                else:
                    return redirect("client-dashboard")
    else:
        form = AuthenticationForm()

    return render(request, "account/login.html", {"login_form": form})


def user_logout(request):
    logout(request)
    return redirect("login")


def email_verification(request, uidb64, token):
    unique_token = force_str(urlsafe_base64_decode(uidb64))
    custom_user = CustomUser.objects.get(pk=unique_token)
    if custom_user and user_tokenize_generator.check_token(
        custom_user, token
    ):  # basically checking to see if that token with that id is associated with a particular user
        custom_user.is_active = True
        custom_user.save()
        return redirect("email_verification_success")
    return redirect("email_verification_failed")


def email_verification_sent(request):
    return render(request, "account/email-verification-sent.html")


def email_verification_failed(request):
    return render(request, "account/email-verification-success.html")


def email_verification_successful(request):
    return render(request, "account/email-verification-failed.html")

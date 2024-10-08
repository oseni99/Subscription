from django.contrib.auth import views as auth_views
from django.urls import path

from . import views

urlpatterns = [
    path("", views.home_page, name="home"),
    path("register", views.register, name="register"),
    path("login", views.my_login, name="login"),
    path("user-logout", views.user_logout, name="user_logout"),
    # Password reset urls management
    # 1 - Request password reset email
    path(
        "password_reset/",
        auth_views.PasswordResetView.as_view(
            template_name="account/password_reset.html",
            email_template_name="account/password_reset_email.html",
            subject_template_name="account/password_reset_subject.txt",
            success_url="/password_reset/done",
        ),
        name="password_reset",
    ),
    # 2 - Password reset email sent success mssg
    path(
        "password_reset/done/",
        auth_views.PasswordResetDoneView.as_view(
            template_name="account/password_reset_done.html"
        ),
        name="password_reset_done",
    ),
    # 3 - reset password itself page as we enter a new password
    path(
        "password_reset/confirm/<uidb64>/<token>/",
        auth_views.PasswordResetConfirmView.as_view(
            template_name="account/password_reset_confirm.html"
        ),
        name="password_reset_confirm",
    ),
    # 4 - password reset success mssg
    path(
        "password_reset/complete/",
        auth_views.PasswordResetCompleteView.as_view(
            template_name="account/password_reset_complete.html"
        ),
        name="password_reset_complete",
    ),
    # Email verification urls managemen
    path(
        "email_verification/<uidb64>/<token>/",
        views.email_verification,
        name="email_verification",
    ),
    path(
        "email_verification_sent",
        views.email_verification_sent,
        name="email_verification_sent",
    ),
    path(
        "email_verification_success",
        views.email_verification_successful,
        name="email_verification_success",
    ),
    path(
        "email_verification_failed",
        views.email_verification_failed,
        name="email_verification_failed",
    ),
]

from django.db import models

from django.utils.translation import gettext_lazy as _ 
from .managers import CustomUserManager
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils import timezone

class CustomUser(AbstractBaseUser, PermissionsMixin):
    username = None 
    email = models.EmailField(_("Email Address"), max_length=254,unique=True)
    first_name = models.CharField(_("First Name"), max_length=80)
    last_name = models.CharField(_("Last Name"), max_length=120)
    is_active = models.BooleanField(_("Is Active"),default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(_("Date Joined"), default=timezone.now)
    is_writer = models.BooleanField(default=False, verbose_name="Are you a writer?")
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []


    objects = CustomUserManager()

    def __str__(self):
        return self.email
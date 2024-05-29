from django.db import models
from account.models import CustomUser

class Article(models.Model):

    title = models.CharField(max_length=200)
    content = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)
    is_premium = models.BooleanField(verbose_name="Is This Premium?")

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, max_length=15, null=True)
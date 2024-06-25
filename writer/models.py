from django.db import models
from account.models import CustomUser

class Article(models.Model):

    title = models.CharField(max_length=200) 
    content = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)
    is_premium = models.BooleanField(verbose_name="Is This Premium?")
    date_edited = models.DateTimeField(verbose_name="Edited Date", auto_now=True, auto_now_add=False)

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True)

    class Meta:
        ordering = ['-date_posted']
        constraints = [
            models.UniqueConstraint(fields=['title','user'], name='Unique_title_user')
            ]

    def __str__(self):
        premium_status = "Premium" if self.is_premium else "Basic"
        return f"{self.title} --> {premium_status}"
    
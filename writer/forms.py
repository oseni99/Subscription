from django import forms 
from .models import Article
from account.models import CustomUser


class ArticleForm(forms.ModelForm):
    
    class Meta:
        model = Article
        fields = [
            "title","content","is_premium",
            ]

class UpdateUserForm(forms.ModelForm):
    # password = None #

    class Meta:
        model = CustomUser
        fields = [
            "email","first_name","last_name",
            ]
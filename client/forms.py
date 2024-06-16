from django import forms 
from account.models import CustomUser


class UpdateUserForm(forms.ModelForm):
    
    class Meta:
        model = CustomUser
        fields = [
            "email","first_name","last_name"
          ]

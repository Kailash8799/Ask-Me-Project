from django import forms
from django.forms import ModelForm
from user_auth.models import Users

class UsersForm(forms.ModelForm):
    
    class Meta:
        model = Users
        fields = ("__all__")

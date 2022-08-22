from dataclasses import fields
from django import forms
from .models import users_details

class User(forms.ModelForm):
    class Meta:
        model = users_details
        fields = "__all__"
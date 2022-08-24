from dataclasses import fields
from django import forms
from .models import kontrol

class Login_pager(forms.ModelForm):
    class Meta:
        model = kontrol
        fields = "__all__"
from dataclasses import field, fields
from django import forms
from .models import yeniEnvanter
class Yeni(forms.ModelForm):
    class Meta:
        model = yeniEnvanter
        fields = "__all__"
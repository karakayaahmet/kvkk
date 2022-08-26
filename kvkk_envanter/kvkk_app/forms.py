
from dataclasses import fields
from pyexpat import model
from django import forms
from .models import Tum_Envanter
class PostForm(forms.ModelForm):
    class Meta:
        model = Tum_Envanter
        fields = "__all__"
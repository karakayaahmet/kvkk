from dataclasses import fields
from pyexpat import model
from django import forms
from .models import Kayitli_işlen_amac
class Amaclar(forms.ModelForm):
    class Meta:
        model = Kayitli_işlen_amac
        fields = "__all__"
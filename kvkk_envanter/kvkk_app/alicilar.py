from dataclasses import fields
from pyexpat import model
from django import forms
from .models import Kayitli_alicilar
class Alicilar(forms.ModelForm):
    class Meta:
        model = Kayitli_alicilar
        fields = "__all__"
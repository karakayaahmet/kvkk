from dataclasses import fields
from pyexpat import model
from django import forms
from .models import Kayitli_kisisel_veriler
class Kisisel_Veriler(forms.ModelForm):
    class Meta:
        model = Kayitli_kisisel_veriler
        fields = "__all__"
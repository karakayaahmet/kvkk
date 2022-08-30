from dataclasses import fields
from pyexpat import model
from django import forms
from .models import Kayili_kisisel_ver_isl_kisiler
class Kisiler(forms.ModelForm):
    class Meta:
        model = Kayili_kisisel_ver_isl_kisiler
        fields = "__all__"
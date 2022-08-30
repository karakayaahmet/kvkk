from dataclasses import fields
from pyexpat import model
from django import forms
from .models import Kayitli_tum_veriler
class Tum_Veriler(forms.ModelForm):
    class Meta:
        model = Kayitli_tum_veriler
        fields = "__all__"
from dataclasses import fields
from pyexpat import model
from django import forms
from .models import Kayitli_ozel_veriler
class Ozel_Veriler(forms.ModelForm):
    class Meta:
        model = Kayitli_ozel_veriler
        fields = "__all__"
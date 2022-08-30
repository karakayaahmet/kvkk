from dataclasses import fields
from pyexpat import model
from django import forms
from .models import Kayitli_guv_onl
class Guvenlik(forms.ModelForm):
    class Meta:
        model = Kayitli_guv_onl
        fields = "__all__"
from dataclasses import fields
from pyexpat import model
from django import forms
from .models import Kayitli_org_yetkili
class Yetkili(forms.ModelForm):
    class Meta:
        model = Kayitli_org_yetkili
        fields = "__all__"
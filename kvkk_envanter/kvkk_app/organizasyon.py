
from dataclasses import fields
from pyexpat import model
from django import forms
from .models import Kayitli_org_isim
class Organizasyon(forms.ModelForm):
    class Meta:
        model = Kayitli_org_isim
        fields = "__all__"
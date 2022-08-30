from dataclasses import fields
from pyexpat import model
from django import forms
from .models import Kayitli_top_yontem
class Yontemler(forms.ModelForm):
    class Meta:
        model = Kayitli_top_yontem
        fields = "__all__"
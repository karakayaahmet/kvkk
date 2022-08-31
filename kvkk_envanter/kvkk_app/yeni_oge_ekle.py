
from dataclasses import fields
from pyexpat import model
from django import forms
from .models import Kayili_kisisel_ver_isl_kisiler, Kayitli_alicilar, Kayitli_guv_onl, Kayitli_kisisel_veriler, Kayitli_org_isim, Kayitli_org_yetkili, Kayitli_ozel_veriler, Kayitli_top_yontem, Kayitli_tum_veriler, Kayitli_işlen_amac
class Organizasyon(forms.ModelForm):
    class Meta:
        model = Kayitli_org_isim
        fields = "__all__"

class Yetkili(forms.ModelForm):
    class Meta:
        model = Kayitli_org_yetkili
        fields = "__all__"

class Alicilar(forms.ModelForm):
    class Meta:
        model = Kayitli_alicilar
        fields = "__all__"

class Kisiler(forms.ModelForm):
    class Meta:
        model = Kayili_kisisel_ver_isl_kisiler
        fields = "__all__"

class Guvenlik(forms.ModelForm):
    class Meta:
        model = Kayitli_guv_onl
        fields = "__all__"

class Ozel_Veriler(forms.ModelForm):
    class Meta:
        model = Kayitli_ozel_veriler
        fields = "__all__"

class Kisisel_Veriler(forms.ModelForm):
    class Meta:
        model = Kayitli_kisisel_veriler
        fields = "__all__"

class Tum_Veriler(forms.ModelForm):
    class Meta:
        model = Kayitli_tum_veriler
        fields = "__all__"

class Yontemler(forms.ModelForm):
    class Meta:
        model = Kayitli_top_yontem
        fields = "__all__"

class Amaclar(forms.ModelForm):
    class Meta:
        model = Kayitli_işlen_amac
        fields = "__all__"


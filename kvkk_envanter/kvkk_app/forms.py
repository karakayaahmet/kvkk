
from dataclasses import fields
from pyexpat import model
from django import forms
from .models import Tum_Envanter
class PostForm(forms.ModelForm):
    class Meta:
        model = Tum_Envanter
        fields = "departman_ismi","yetkili","is_sureci","veri_isleme_faaliyeti","kisisel_verisi_islenen_kisi","kisisel_verinin_toplanma_yontemi","islenen_tum_veriler","islenen_kisisel_veriler","islenen_ozel_nitelikli_veriler","gerekli_olmayan_veriler","amac","alici_gruplari_ic","paylasim_amaci","alici_gruplari_dis","paylasilan_veriler","paylasilan_ulkeler","paylasim_amaclari","hukuksal_dayanak","tum_tedbirler","islenen_sure","saklanilan_yer","erisen_kisiler"
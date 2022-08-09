import imp
from django.contrib import admin
from .models import users_details,Organizasyon,Surec,Saklama,Islenen_Veriler, Tum_Envanter,Yurtdisi_Aktarim,Yurtici_Aktarim,Hukuksal_Dayanak,Guvenlik_Tedbirleri,Kayitli_alicilar,Kayitli_guv_onl,Kayitli_işlen_amac,Kayitli_org_isim,Kayitli_top_yontem,Kayitli_kisisel_veriler,Kayitli_org_yetkili,Kayitli_ozel_veriler,Kayitli_tum_veriler
# Register your models here.
admin.site.register(Organizasyon)
admin.site.register(Surec)
admin.site.register(Saklama)
admin.site.register(Islenen_Veriler)
admin.site.register(Yurtdisi_Aktarim)
admin.site.register(Yurtici_Aktarim)
admin.site.register(Hukuksal_Dayanak)
admin.site.register(Guvenlik_Tedbirleri)
admin.site.register(Kayitli_tum_veriler)
admin.site.register(Kayitli_alicilar)
admin.site.register(Kayitli_işlen_amac)
admin.site.register(Kayitli_guv_onl)
admin.site.register(Kayitli_top_yontem)
admin.site.register(Kayitli_org_isim)
admin.site.register(Kayitli_org_yetkili)
admin.site.register(Kayitli_kisisel_veriler)
admin.site.register(Kayitli_ozel_veriler)
admin.site.register(Tum_Envanter)
admin.site.register(users_details)



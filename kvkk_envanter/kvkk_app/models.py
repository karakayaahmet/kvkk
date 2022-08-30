from django.db import models

# Create your models here.
from operator import truediv
from platform import mac_ver
from pyexpat import model
from django.db import models

# Create your models here.

class Kayili_kisisel_ver_isl_kisiler(models.Model):
    kisiler = models.CharField(max_length=100,blank=True)


class Tum_Envanter(models.Model):
    departman_ismi = models.CharField(max_length=70)
    yetkili = models.CharField(max_length=30)
    is_sureci = models.TextField(max_length=100)
    veri_isleme_faaliyeti = models.TextField(max_length=200)
    kisisel_verisi_islenen_kisi = models.CharField(max_length=40)
    kisisel_verinin_toplanma_yontemi = models.CharField(max_length=100)
    islenen_tum_veriler = models.TextField(max_length=1000)
    islenen_kisisel_veriler = models.TextField(max_length=1000)
    islenen_ozel_nitelikli_veriler = models.TextField(max_length=1000, blank=True)
    gerekli_olmayan_veriler = models.TextField(max_length=500)
    amac = models.TextField(max_length=1000)
    alici_gruplari_ic = models.TextField(max_length=200)
    paylasim_amaci = models.TextField(max_length=200)
    alici_gruplari_dis= models.TextField(max_length=200)
    paylasilan_veriler = models.TextField(max_length=200)
    paylasilan_ulkeler = models.TextField(max_length=100)
    paylasim_amaclari = models.TextField(max_length=200)
    hukuksal_dayanak= models.TextField(max_length=100, blank=True)
    tum_tedbirler = models.TextField(max_length=3000)
    saklanilan_yer = models.TextField(max_length=100)
    islenen_sure = models.CharField(max_length=100)
    erisebilen_kisiler = models.CharField(max_length=100)


class Kayitli_guv_onl(models.Model):
    tedbir = models.TextField(max_length=200)

    def __str__(self):
        return self.tedbir

class Kayitli_org_isim(models.Model):
    isim = models.TextField(max_length=50, blank=True)

    def __str__(self):
        return self.isim

class Kayitli_org_yetkili(models.Model):
    yetkili = models.TextField(max_length=50, blank=True)

    def __str__(self):
        return self.yetkili

class Kayitli_tum_veriler(models.Model):
    kisisel_tum_veriler = models.TextField(max_length=50, blank=True)

    def __str__(self):
        return self.kisisel_tum_veriler

class Kayitli_kisisel_veriler(models.Model):
    kisisel_veriler = models.TextField(max_length=50, blank=True)

    def __str__(self):
        return self.kisisel_veriler

class Kayitli_ozel_veriler(models.Model):
    ozel_kisisel_veriler = models.TextField(max_length=50, blank=True)

    def __str__(self):
        return self.ozel_kisisel_veriler

class Kayitli_top_yontem(models.Model):
    yontemler = models.TextField(max_length=100,blank=True)

    def __str__(self):
        return self.yontemler

class Kayitli_işlen_amac(models.Model):
    amaclar = models.TextField(max_length=100, blank=True)

    def __str__(self):
        return self.amaclar

class Kayitli_alicilar(models.Model):
    alicilar = models.TextField(max_length=50, blank=True)

    def __str__(self):
        return self.alicilar


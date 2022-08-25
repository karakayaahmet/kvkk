from django.db import models

# Create your models here.
from operator import truediv
from platform import mac_ver
from pyexpat import model
from django.db import models

# Create your models here.

class kontrol(models.Model):
    email = models.CharField(max_length=30)
    sifre = models.CharField(max_length=30)

class users_details(models.Model):
    kullanici_adi = models.CharField(max_length=30)
    tel = models.CharField(max_length=11)
    kurum_adi = models.CharField(max_length=75)
    email = models.CharField(max_length=30)
    sifre = models.CharField(max_length=15)

class Tum_Envanter(models.Model):
    departman_ismi = models.CharField(max_length=70,blank=True)
    yetkili = models.CharField(max_length=30,blank=True)
    is_sureci = models.TextField(max_length=100, blank=True)
    veri_isleme_faaliyeti = models.TextField(max_length=200, blank=True)
    kisisel_verisi_islenen_kisi = models.CharField(max_length=40, blank=True)
    kisisel_verinin_toplanma_yontemi = models.CharField(max_length=100, blank=True)
    islenen_tum_veriler = models.TextField(max_length=1000, blank=True)
    islenen_kisisel_veriler = models.TextField(max_length=1000, blank=True)
    islenen_ozel_nitelikli_veriler = models.TextField(max_length=1000, blank=True)
    gerekli_olmayan_veriler = models.TextField(max_length=500, blank=True)
    amac = models.TextField(max_length=1000, blank=True)
    alici_gruplari_ic = models.TextField(max_length=200, blank=True)
    paylasim_amaci = models.TextField(max_length=200, blank=True)
    alici_gruplari_dis= models.TextField(max_length=200, blank=True)
    paylasilan_veriler = models.TextField(max_length=200, blank=True)
    paylasilan_ulkeler = models.TextField(max_length=100, blank=True)
    paylasim_amaclari = models.TextField(max_length=200, blank=True)
    hukuksal_dayanak= models.TextField(max_length=100, blank=True)
    tum_tedbirler = models.TextField(max_length=3000, blank=True)


class Organizasyon(models.Model):
    departman_ismi = models.CharField(max_length=70,blank=True)
    yetkili = models.CharField(max_length=30,blank=True)

class Surec(models.Model):
    is_sureci = models.TextField(max_length=100, blank=True)
    veri_isleme_faaliyeti = models.TextField(max_length=200, blank=True)
    kisisel_verisi_islenen_kisi = models.CharField(max_length=40, blank=True)
    kisisel_verinin_toplanma_yontemi = models.CharField(max_length=100, blank=True)

class Islenen_Veriler(models.Model):
    islenen_tum_veriler = models.TextField(max_length=1000, blank=True)
    islenen_kisisel_veriler = models.TextField(max_length=1000, blank=True)
    islenen_ozel_nitelikli_veriler = models.TextField(max_length=1000, blank=True)
    gerekli_olmayan_veriler = models.TextField(max_length=500, blank=True)
    amac = models.TextField(max_length=1000, blank=True)

class Yurtici_Aktarim(models.Model):
    alici_gruplari = models.TextField(max_length=200, blank=True)
    paylasim_amaci = models.TextField(max_length=200, blank=True)

class Yurtdisi_Aktarim(models.Model):
    alici_gruplari= models.TextField(max_length=200, blank=True)
    paylasilan_veriler = models.TextField(max_length=200, blank=True)
    paylasilan_ulkeler = models.TextField(max_length=100, blank=True)
    paylasim_amaclari = models.TextField(max_length=200, blank=True)

class Saklama(models.Model):
    saklanilan_sure = models.CharField(max_length=15, blank=True)
    saklanilan_yer = models.TextField(max_length=100, blank=True)
    verilere_erişebilen_kisiler = models.TextField(max_length=100, blank=True)

class Hukuksal_Dayanak(models.Model):
    hukuksal_dayanak= models.TextField(max_length=100, blank=True)

class Guvenlik_Tedbirleri(models.Model):
    tum_tedbirler = models.TextField(max_length=3000, blank=True)

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


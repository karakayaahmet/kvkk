
from ast import Or
import email
from email import contentmanager
import imp
import re
from tkinter.messagebox import NO
from unicodedata import name
from django.shortcuts import render
from .models import Kayili_kisisel_ver_isl_kisiler,Tum_Envanter,Kayitli_org_isim,Kayitli_org_yetkili, Kayitli_top_yontem,Kayitli_tum_veriler,Kayitli_kisisel_veriler,Kayitli_ozel_veriler,Kayitli_işlen_amac,Kayitli_alicilar,Kayitli_guv_onl
from .forms import PostForm
from .yeni_oge_ekle import Amaclar, Guvenlik, Kisisel_Veriler, Organizasyon, Ozel_Veriler, Tum_Veriler, Yetkili, Alicilar, Kisiler, Yontemler


def kayitlar(request):
    emailler = Tum_Envanter.objects.all()
    return render(request,"kvkk_app/kayitlar.html",{"emailler":emailler})

def anasayfa(request):
    return render(request,"kvkk_app/anasayfa.html")

def veri_giris(request):
    context = {}
    context["emailler"] = Tum_Envanter.objects.all()
    context["listem"] = Kayitli_org_isim.objects.all()
    context["yetkili"] = Kayitli_org_yetkili.objects.all()
    context["tum_veriler"] = Kayitli_tum_veriler.objects.all()
    context["kisisel_veriler"] = Kayitli_kisisel_veriler.objects.all() 
    context["ozel_veriler"] = Kayitli_ozel_veriler.objects.all()
    context["amaclar"] = Kayitli_işlen_amac.objects.all()
    context["alicilar"] = Kayitli_alicilar.objects.all()
    context["tedbirler"] = Kayitli_guv_onl.objects.all()
    context["top_yontem"] = Kayitli_top_yontem.objects.all()
    context["kisiler"] = Kayili_kisisel_ver_isl_kisiler.objects.all()
    
    # submitting two forms from one views new
    # if request.method == "POST":
    #     post_form = PostForm(request.POST or None)
    #     organizasyion_form = Organizasyon(request.POST)
    #     if post_form.is_valid() and organizasyion_form.is_valid():
    #         post_form.save()
    #         organizasyion_form.save()
    #         context["yetkili"] = Kayitli_org_yetkili.objects.all()
    #         context["tum_veriler"] = Kayitli_tum_veriler.objects.all()
    #         context["kisisel_veriler"] = Kayitli_kisisel_veriler.objects.all() 
    #         context["ozel_veriler"] = Kayitli_ozel_veriler.objects.all()
    #         context["amaclar"] = Kayitli_işlen_amac.objects.all()
    #         context["alicilar"] = Kayitli_alicilar.objects.all()
    #         context["tedbirler"] = Kayitli_guv_onl.objects.all()
    #         context["top_yontem"] = Kayitli_top_yontem.objects.all()
    #         context["kisiler"] = Kayili_kisisel_ver_isl_kisiler.objects.all()
    #         context["listem"] = Kayitli_org_isim.objects.all()
    #         return render(request,"kvkk_app/veri_giris.html",context)
    # else:
    #     post_form = PostForm()
    #     organizasyion_form = Organizasyon()
    #     return render(request,"kvkk_app/veri_giris.html",context)  


# 30 ağustos sonu yöntemimiz:
    # if request.method == 'POST':
    #     post_form = PostForm(request.POST or None)
    #     organizasyon_form = Organizasyon(request.POST or None)
    #     yetkili_form = Yetkili(request.POST or None)
    #     alicilar_form = Alicilar(request.POST or None)
    #     kisiler_form = Kisiler(request.POST or None)
    #     guvenlik_form = Guvenlik(request.POST or None)
    #     Ozel_Veriler_form = Ozel_Veriler(request.POST or None)
    #     kisisel_veriler_form =  Kisisel_Veriler(request.POST or None)
    #     tum_veriler_form = Tum_Veriler(request.POST or None)
    #     toplanma_yontemleri_form = Yontemler(request.POST or None)
    #     islenme_amaclari_form = Amaclar(request.POST or None)

    #     if organizasyon_form.is_valid():
    #         organizasyon_form.save()
    #         context["listem"] = Kayitli_org_isim.objects.all()

    #     if yetkili_form.is_valid():
    #         yetkili_form.save()
    #         context["yetkili"] = Kayitli_org_yetkili.objects.all()

    #     if alicilar_form.is_valid():
    #         alicilar_form.save()
    #         context["alicilar"] = Kayitli_alicilar.objects.all()

    #     if kisiler_form.is_valid():
    #         kisiler_form.save()
    #         context["kisiler"] = Kayili_kisisel_ver_isl_kisiler.objects.all()

    #     if guvenlik_form.is_valid():
    #         guvenlik_form.save()
    #         context["tedbirler"] = Kayitli_guv_onl.objects.all()

    #     if Ozel_Veriler_form.is_valid():
    #         Ozel_Veriler_form.save()
    #         context["ozel_veriler"] = Kayitli_ozel_veriler.objects.all()

    #     if kisisel_veriler_form.is_valid():
    #         kisisel_veriler_form.save()
    #         context["kisisel_veriler"] = Kayitli_kisisel_veriler.objects.all() 

    #     if tum_veriler_form.is_valid():
    #         tum_veriler_form.save()
    #         context["tum_veriler"] = Kayitli_tum_veriler.objects.all()

    #     if toplanma_yontemleri_form.is_valid():
    #         toplanma_yontemleri_form.save()
    #         context["top_yontem"] = Kayitli_top_yontem.objects.all()

    #     if islenme_amaclari_form.is_valid():
    #         islenme_amaclari_form.save()
    #         context["amaclar"] = Kayitli_işlen_amac.objects.all()

    #     if organizasyon_form.is_valid() and yetkili_form.is_valid() and alicilar_form.is_valid() and kisiler_form.is_valid() and guvenlik_form.is_valid() and Ozel_Veriler_form.is_valid() and kisisel_veriler_form.is_valid() and tum_veriler_form.is_valid() and toplanma_yontemleri_form.is_valid() and islenme_amaclari_form.is_valid() and post_form.is_valid() : 
    #         post_form.save()
    #         context["emailler"] = Tum_Envanter.objects.all()
    #         return render(request,"kvkk_app/veri_giris.html",context)

    #     else:
    #         return render(request,"kvkk_app/veri_giris.html",context)

    # else:
    #     return render(request,"kvkk_app/veri_giris.html",context)
# 30 ağustos sonu yöntemimiz sonu

# 31 ağustos yöntemimiz:

    if request.method == 'POST':
        post_form = PostForm(request.POST or None)
        organizasyion_form = Organizasyon(request.POST)
        yetkili_form = Yetkili(request.POST)
        alicilar_form = Alicilar(request.POST)
        kisiler_form = Kisiler(request.POST)
        guvenlik_form = Guvenlik(request.POST)
        Ozel_Veriler_form = Ozel_Veriler(request.POST)
        kisisel_veriler_form =  Kisisel_Veriler(request.POST)
        tum_veriler_form = Tum_Veriler(request.POST)
        toplanma_yontemleri_form = Yontemler(request.POST)
        islenme_amaclari_form = Amaclar(request.POST)
        if request.POST.get("isim") == 'departman-ismi-id':
            organizasyion_form.save()
        elif request.POST.get("yetkili") == 'bilgi-girisi-yapan-kisi-id':
            yetkili_form.save()
        elif request.POST.get("kisiler") == 'kisisel-verisi-islenen-kisi-id':
            kisiler_form.save()
        elif request.POST.get("yontemler") == 'veri-toplanma-yontemi-id':
            toplanma_yontemleri_form.save()
        elif request.POST.get("kisisel_tum_veriler") == 'islenen-veriler-id':
            tum_veriler_form.save()
        elif request.POST.get("kisisel_veriler") == 'kisisel-veriler-id':
            kisisel_veriler_form.save()
        elif request.POST.get("ozel_kisisel_veriler") == 'ozel-veriler-id':
            Ozel_Veriler_form.save()
        elif request.POST.get("kisisel_tum_veriler") == 'gerekli-olmayan-veriler-id':
            tum_veriler_form.save()
        elif request.POST.get("alicilar") == 'alici-gruplari-ic-id':
            alicilar_form.save()
        elif request.POST.get("amaclar") == 'paylasim-amaci-ic-id':
            islenme_amaclari_form.save()
        elif request.POST.get("alicilar") == 'alici-gruplari-dis-id':
            alicilar_form.save()
        elif request.POST.get("amaclar") == 'paylasim-amaci-dis-id':
            islenme_amaclari_form.save()
        elif request.POST.get("kisisel_tum_veriler") == 'yurt-disine-paylasilan-veriler-id':
            tum_veriler_form.save()
        elif request.POST.get("tedbir") == 'Alinan-tedbirler-id':
            guvenlik_form.save()
        elif post_form.is_valid():
            post_form.save()
            context["emailler"] = Tum_Envanter.objects.all()
            return render(request,"kvkk_app/veri_giris.html",context)
    else:
        return render(request,"kvkk_app/veri_giris.html",context)
        
    # submitting twenty forms from one views new
    # if request.method == "POST":
    #     post_form = PostForm(request.POST or None)
    #     organizasyion_form = Organizasyon(request.POST)
    #     yetkili_form = Yetkili(request.POST)
    #     alicilar_form = Alicilar(request.POST)
    #     kisiler_form = Kisiler(request.POST)
    #     guvenlik_form = Guvenlik(request.POST)
    #     Ozel_Veriler_form = Ozel_Veriler(request.POST)
    #     kisisel_veriler_form =  Kisisel_Veriler(request.POST)
    #     tum_veriler_form = Tum_Veriler(request.POST)
    #     toplanma_yontemleri_form = Yontemler(request.POST)
    #     islenme_amaclari_form = Amaclar(request.POST)
    #     if post_form.is_valid() and organizasyion_form.is_valid() and yetkili_form.is_valid() and alicilar_form.is_valid() and kisiler_form.is_valid() and guvenlik_form.is_valid() and Ozel_Veriler_form.is_valid() and kisisel_veriler_form.is_valid() and tum_veriler_form.is_valid() and toplanma_yontemleri_form.is_valid() and islenme_amaclari_form.is_valid():
    #         post_form.save()
    #         organizasyion_form.save()
    #         yetkili_form.save()
    #         alicilar_form.save()
    #         kisiler_form.save()
    #         guvenlik_form.save()
    #         Ozel_Veriler_form.save()
    #         kisisel_veriler_form.save()
    #         tum_veriler_form.save()
    #         toplanma_yontemleri_form.save()
    #         islenme_amaclari_form.save()
    #         return render(request,"kvkk_app/veri_giris.html",context)
    #     else:
    #         return render(request,"kvkk_app/veri_giris.html",context)
    # else:
    #     return render(request,"kvkk_app/veri_giris.html",context)



    # return render(request,"kvkk_app/veri_giris.html",{"form":post_form,"form2":organizasyion_form})

    
    # if request.method == 'POST':
    #     form = PostForm(request.POST or None)
    #     if form.is_valid():
    #         form.save()
            
    #         return render(request,"kvkk_app/veri_giris.html",context)
    
    # else:
        
    #     return render(request,"kvkk_app/veri_giris.html",context)




def profil(request):
    return render(request,"kvkk_app/profil.html")


        

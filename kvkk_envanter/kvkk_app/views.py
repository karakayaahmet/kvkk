
import email
from email import contentmanager
import re
from unicodedata import name
from django.shortcuts import render
from .models import Kayili_kisisel_ver_isl_kisiler, kontrol,users_details,Tum_Envanter,Kayitli_org_isim,Kayitli_org_yetkili, Kayitli_top_yontem,Kayitli_tum_veriler,Kayitli_kisisel_veriler,Kayitli_ozel_veriler,Kayitli_işlen_amac,Kayitli_alicilar,Kayitli_guv_onl,Organizasyon
from .forms import PostForm
from .form2 import User
from .login import Login_pager
# Create your views here.

def envanter(request):
    
            
    if request.method == 'POST':
        form = PostForm(request.POST or None)
        if form.is_valid():
            form.save()
            context = {}
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
            return render(request,"kvkk_app/verigiris.html",context)
              
    else:
        context = {}
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
        return render(request,"kvkk_app/envanter.html",context)


def kayitlar(request):
    emailler = Tum_Envanter.objects.all()
    return render(request,"kvkk_app/kayitlar.html",{"emailler":emailler})

def anasayfa(request):
    return render(request,"kvkk_app/anasayfa.html")

def veri_giris(request):
    if request.method == 'POST':
        form = PostForm(request.POST or None)
        if form.is_valid():
            form.save()
            context = {}
            context["listem"] = Tum_Envanter.objects.all()
            context["yetkili"] = Kayitli_org_yetkili.objects.all()
            context["tum_veriler"] = Kayitli_tum_veriler.objects.all()
            context["kisisel_veriler"] = Kayitli_kisisel_veriler.objects.all() 
            context["ozel_veriler"] = Kayitli_ozel_veriler.objects.all()
            context["amaclar"] = Kayitli_işlen_amac.objects.all()
            context["alicilar"] = Kayitli_alicilar.objects.all()
            context["tedbirler"] = Kayitli_guv_onl.objects.all()
            context["top_yontem"] = Kayitli_top_yontem.objects.all()
            context["kisiler"] = Kayili_kisisel_ver_isl_kisiler.objects.all()
            return render(request,"kvkk_app/veri_giris.html",context)
    
    else:
        context = {}
        context["listem"] = Tum_Envanter.objects.all()
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
        return render(request,"kvkk_app/veri_giris.html",context)

def kayit(request):
    tum_verilerim = Tum_Envanter.objects.all()
    return render(request,"kvkk_app/kayit.html",{"tum_verilerim":tum_verilerim})

        

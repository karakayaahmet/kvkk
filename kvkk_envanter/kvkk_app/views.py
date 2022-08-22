
import email
from email import contentmanager
import re
from unicodedata import name
from django.shortcuts import render
from .models import users_details,Tum_Envanter,Kayitli_org_isim,Kayitli_org_yetkili, Kayitli_top_yontem,Kayitli_tum_veriler,Kayitli_kisisel_veriler,Kayitli_ozel_veriler,Kayitli_işlen_amac,Kayitli_alicilar,Kayitli_guv_onl,Organizasyon
from .forms import PostForm
from .form2 import User
# Create your views here.

def giris(request):
    context = {}
    
    context["email_sifre"] = users_details.objects.all()
    if request.method == 'POST':
        form = User(request.POST or None)
        if form.is_valid():
            form.save()
            veriler = users_details.objects.all()
            return render(request,"kvkk_app/giris.html",{"veriler":veriler})
    else:
        return render(request,"kvkk_app/giris.html",context)
    
    
    


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
            context["contex"] =Organizasyon.objects.all()
            return render(request,"kvkk_app/envanter.html",context)
              
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
        context["contex"] =Organizasyon.objects.all()
        return render(request,"kvkk_app/envanter.html",context)

def kayit(request):
    emailler = users_details.objects.all()
    return render(request,"kvkk_app/kayit.html",{"emailler":emailler})

def anasayfa(request):
    return render(request,"kvkk_app/anasayfa.html")

def veri_giris(request):
    return render(request,"kvkk_app/veri_giris.html")
        

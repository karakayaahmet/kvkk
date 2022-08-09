
from django.shortcuts import render
from .models import users_details,Tum_Envanter,Kayitli_org_isim,Kayitli_org_yetkili, Kayitli_top_yontem,Kayitli_tum_veriler,Kayitli_kisisel_veriler,Kayitli_ozel_veriler,Kayitli_işlen_amac,Kayitli_alicilar,Kayitli_guv_onl,Organizasyon
from .forms import PostForm
# Create your views here.

def giris(request):
    if request.method == 'POST':
        form = PostForm(request.POST or None)
        if form.is_valid():
            form.save()
            veriler = users_details.objects.all()
            return render(request,"kvkk_app/giris.html",{"veriler":veriler})
    else:
        return render(request,"kvkk_app/giris.html")

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
    tum_verilerim = Tum_Envanter.objects.all()
    return render(request,"kvkk_app/kayit.html",{"tum_verilerim":tum_verilerim})
        

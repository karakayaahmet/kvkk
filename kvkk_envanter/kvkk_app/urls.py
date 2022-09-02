
from django.urls import path
from . import views

urlpatterns = [
    
    path('/profil',views.profil, name="profil"),
    path('/kayitlar',views.kayitlar, name="kayitlar"),
    path('/anasayfa',views.anasayfa, name="anasayfa"),
    path('/verigiris',views.veri_giris, name="veri_giris"),
    path('/verbis',views.verbis, name="verbis")

]
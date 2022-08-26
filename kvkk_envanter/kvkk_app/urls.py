
from django.urls import path
from . import views

urlpatterns = [
    
    path('envanter/',views.envanter,name="envanter"),
    path('kayitlar/',views.kayitlar, name="kayitlar"),
    path('anasayfa/',views.anasayfa, name="anasayfa"),
    path('verigiris/',views.veri_giris, name="veri_giris")
]

from django.urls import path
from . import views

urlpatterns = [
    path('',views.giris, name="giris"),
    path('envanter/',views.envanter,name="envanter"),
    path('kayit/',views.kayit, name="kayit"),
    path('anasayfa/',views.anasayfa, name="anasayfa"),
    path('verigiris/',views.veri_giris, name="veri_giris")
]
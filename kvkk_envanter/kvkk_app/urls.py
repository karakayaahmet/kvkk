
from django.urls import path
from . import views

urlpatterns = [
    
    path('envanter/',views.envanter,name="envanter"),
<<<<<<< Updated upstream
    path('kayitlar/',views.kayitlar, name="kayitlar"),
    path('anasayfa/',views.anasayfa, name="anasayfa"),
    path('verigiris/',views.veri_giris, name="veri_giris")
=======
    path('kayit/',views.kayit, name="kayit"),
    path('base/',views.base, name='base')
>>>>>>> Stashed changes
]
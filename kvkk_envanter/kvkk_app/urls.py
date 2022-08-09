
from django.urls import path
from . import views

urlpatterns = [
    path('',views.giris, name="giris"),
    path('envanter/',views.envanter,name="envanter"),
    path('kayit/',views.kayit, name="kayit")
]
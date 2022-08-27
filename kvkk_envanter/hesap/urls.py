from django.urls import path
from . import views

urlpatterns = [
    path("",views.login_register_request, name="login"),
    path("/kayitol",views.kayit_request, name="kayitol"),
    path("/logout",views.logout_request, name="logout")
]
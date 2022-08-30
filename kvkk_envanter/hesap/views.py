import email
import imp
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.models import User


def login_register_request(request):

    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("anasayfa")
        else:
            return render(request, "hesap/login.html", {"hata": "Kullanıcı Adı veya Şifre Yanlış"})

    return render(request,"hesap/login.html")


def kayit_request(request):

    if request.method == "POST":
        kurum_adi = request.POST["kurum_adi"]
        username = request.POST["username"]
        tel = request.POST["tel"]
        email = request.POST["email"]
        password = request.POST["password"]
        tekrar_sifre = request.POST["tekrar_sifre"]

        if password == "" and kurum_adi == "" and tel == "" and email == "" and username == "" :
            return render(request,"hesap/kayit_ol.html",{"hata":"Form Boş Bırakılamaz !"})

        if password == tekrar_sifre:
            if User.objects.filter(username=username).exists():
                return render(request, "hesap/kayit_ol.html", {"hata": "Bu Kullanıcı Adı Kullanılıyor.",
                "kurum_adi": kurum_adi,
                "username": username,
                "tel": tel,
                "email": email
                })

            else:
                if User.objects.filter(email=email).exists():
                    return render(request, "hesap/kayit_ol.html", {"hata": "Bu Email Adresi Kullanılıyor.",
                    "kurum_adi": kurum_adi,
                    "username": username,
                    "tel": tel,
                    "emaill": email
                    })

                else:
                    user = User.objects.create_user(
                        username=username, password=password, tel=tel, email=email, kurum_adi=kurum_adi)
                    user.save()
                    return redirect("login")
        else:
            return render(request,"hesap/kayit_ol.html",{"hata":"Parolalar Eşleşmiyor.",
            "kurum_adi": kurum_adi,
            "username": username,
            "tel": tel,
            "emaill": email
            })

    return render(request,"hesap/kayit_ol.html")

def logout_request(request):
    logout(request)
    return redirect("login")



import email
import imp
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
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

    return render(request, "hesap/login.html")


def kayit_request(request):

    if request.method == "POST":
        # kurum_adi = request["kurum_adi"]
        username = request["username"]
        tel = request["tel"]
        email = request["email"]
        password = request["password"]
        tekrar_sifre = request["tekrar_sifre"]

        if password == tekrar_sifre:
            if User.objects.filter(username=username).exists():
                return render(request, "hesap/login.html", {"hata": "Bu Kullanıcı Adı Kullanılıyor.",
                # "kurum_adi": kurum_adi,
                "username": username,
                "tel": tel,
                "email": email
                })

            else:
                if User.objects.filter(email=email).exists():
                    return render(request, "hesap/login.html", {"hata": "Bu Email Adresi Kullanılıyor.",
                    # "kurum_adi": kurum_adi,
                    "username": username,
                    "tel": tel,
                    "emaill": email
                    })

                else:
                    user = User.objects.create_user(
                        username=username, password=password, tel=tel, email=email)
                    user.save()
                    return redirect("")

    return render(request,"hesap/kayit_ol.html")

def logout_request(request):
    return redirect("giris")



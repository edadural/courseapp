from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from account.forms import LoginUserForm
from django.contrib.auth.forms import UserCreationForm

def user_login(request):
    if request.user.is_authenticated and "next" in request.GET:  # kullanıcının login olup olmadığı, icinde next varsa yonlendirmek yerine mesaj
        return render(request, "account/login.html", {"error":"yetkininiz yok"})

    if request.method == "POST":
        form = LoginUserForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                messages.add_message(request, messages.SUCCESS, "Giriş başarılı")
                nextUrl = request.GET.get("next", None)
                if nextUrl is None:
                    return redirect("index")
                else:
                    return redirect(nextUrl)
                
            else:
                return render(request, "account/login.html", {"form":form})
        else:
                return render(request, "account/login.html", {"form":form})
    else:
        form = LoginUserForm()
        return render(request, "account/login.html", {"form":form})

def user_register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()

            username = form.cleaned_data["username"]
            password = form.cleaned_data["password1"]
            user = authenticate(request, username=username, password=password)
            login(request, user)
            return redirect("index")
        else:
            return render(request, "account/register.html", {"form":form})
    else:
        form = UserCreationForm()
        return render(request, "account/register.html", {"form":form})

def user_logout(request):
    messages.add_message(request, messages.SUCCESS, "Çıkış başarılı")
    logout(request)
    return redirect("index")
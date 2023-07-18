from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout

def user_login(request):
    if request.user.is_authenticated:  # kullanıcının login olup olmadığı
        return redirect("index")

    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("index")
        else:
            return render(request, "account/login.html", {"error":"username ya da password yanlış"})

    else:
        return render(request, "account/login.html")

def user_register(request):
    return render(request, "account/register.html")

def user_logout(request):
    logout(request)
    return redirect("index")
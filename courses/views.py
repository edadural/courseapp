from datetime import date, datetime
from django.shortcuts import get_object_or_404, redirect, render
from .models import Course, Category
from django.core.paginator import Paginator

def index(request):
    kurslar = Course.objects.filter(isActive=1, isHome=1)
    kategoriler = Category.objects.all()

    return render(request, 'courses/index.html', {
        'categories': kategoriler,
        'courses': kurslar
    })

def create_course(request):
    if request.method == "POST":
        title = request.POST["title"]
        description = request.POST["description"]
        imageUrl = request.POST["imageUrl"]
        slug = request.POST["slug"]
        isActive = request.POST.get("isActive", False)
        isHome = request.POST.get("isHome", False)
        
        if isActive == "on":
            isActive = True

        if isHome == "on":
            isHome = True

        error = False
        msg = ""

        if title == "":
            error = True
            msg += "Title zorunlu bir alan. "

        if len(title) < 5:
            error = True
            msg += "Title için en az 5 karakter girmelisiniz. "

        if error:
            return render(request, "courses/create-course.html", { "error": True, "msg": msg })

        kurs = Course(title=title, description=description, imageUrl=imageUrl, slug=slug, isActive=isActive, isHome=isHome)
        kurs.save()
        return redirect("/kurslar")
        
    return render(request, "courses/create-course.html")

def search(request):
    if "q" in request.GET and request.GET["q"] != "":
        q = request.GET["q"]
        kurslar = Course.objects.filter(isActive=True, title__contains=q).order_by("date")
        kategoriler = Category.objects.all()
    else:
        return redirect("/kurslar")

    return render(request, 'courses/search.html', {
        'categories': kategoriler,
        'courses': kurslar,
    })

def details(request, slug):
    course = get_object_or_404(Course, slug=slug)  # model icindeki slug = details e gelen slug

    context = {
        'course': course
    }

    return render(request, 'courses/details.html', context)

def getCoursesByCategory(request, slug):
    kurslar = Course.objects.filter(categories__slug=slug, isActive=True).order_by("date")   # aktif olan ve kategorinin slugı gonderilen slugla eslesiyosa kurs bilgileri gelir
    kategoriler = Category.objects.all()

    paginator = Paginator(kurslar, 3)
    page = request.GET.get('page',1)
    page_obj = paginator.page(page)

    return render(request, 'courses/list.html', {
        'categories': kategoriler,
        'page_obj': page_obj,
        'seciliKategori': slug
    })
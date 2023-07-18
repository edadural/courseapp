from django.shortcuts import get_object_or_404, redirect, render
from courses.forms import CourseCreateForm, CourseEditForm
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
        form = form = CourseCreateForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("/kurslar")
    
    else:
        form = CourseCreateForm()
    return render(request, "courses/create-course.html", {"form":form})

def course_list(request):
    kurslar = Course.objects.all()
    return render(request, 'courses/course-list.html', {
        'courses': kurslar
    })

def course_edit(request, id):
    course = get_object_or_404(Course, pk=id)

    if request.method == "POST":
        form = CourseEditForm(request.POST, instance=course)
        form.save()
        return redirect("course_list")
    else:
        form = CourseEditForm(instance=course)  # id ye gore form yuklendiginde, o form uzerine veritabanındaki bilgi yuklenmesi gerekiyo; kullanıcı guncelleyecegi bilgileri form uzerinden gormeli

    return render(request, "courses/edit-course.html", {"form":form})

def course_delete(request, id):
    course = get_object_or_404(Course, pk=id)

    if request.method == "POST":
        course.delete()
        return redirect("course_list")

    return render(request, "courses/course-delete.html", { "course":course })

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
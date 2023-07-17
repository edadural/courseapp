from datetime import date, datetime
from django.http import Http404, HttpResponseNotFound
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from .models import Course, Category

data = {
    "programlama":"programlama kategorisine ait kurslar",
    "web-gelistirme":"web geliştirme kategorisine ait kurslar",
    "mobil":"mobil kategorisine ait kurslar",
}

db = {
    "courses": [
        {
            "title":"javascript kursu",
            "description":"javascript kurs açıklaması",
            "imageUrl":"1.jpg",
            "slug":"javascript-kursu",
            "date":datetime.now(),
            "isActive": True,
            "isUpdated": False
        },
        {
            "title":"python kursu",
            "description":"python kurs açıklaması",
            "imageUrl":"2.jpg",
            "slug":"python-kursu",
            "date":date(2022,9,10),
            "isActive": False,
            "isUpdated": False
        },
        {
            "title":"web geliştirme kursu",
            "description":"web geliştirme kurs açıklaması",
            "imageUrl":"3.jpg",
            "slug":"web-gelistirme-kursu",
            "date":date(2022,8,10),
            "isActive": True,
            "isUpdated": True
        }
    ],
    "categories":[
        { "id":1, "name":"programlama", "slug":"programlama"},
        { "id":2, "name":"web geliştirme", "slug":"web-gelistirme"},
        { "id":3, "name":"mobil uygulamalar", "slug":"mobil-uygulamalar"},
    ]
}

def index(request):
    kurslar = Course.objects.filter(isActive=1)
    kategoriler = Category.objects.all()

    return render(request, 'courses/index.html', {
        'categories': kategoriler,
        'courses': kurslar
    })

def details(request, slug):
    course = get_object_or_404(Course, slug=slug)  # model icindeki slug = details e gelen slug

    context = {
        'course': course
    }

    return render(request, 'courses/details.html', context)

def getCoursesByCategory(request, slug):
    kurslar = Course.objects.filter(category__slug=slug, isActive=True)   # aktif olan ve kategorinin slugı gonderilen slugla eslesiyosa kurs bilgileri gelir
    kategoriler = Category.objects.all()

    return render(request, 'courses/index.html', {
        'categories': kategoriler,
        'courses': kurslar,
        'seciliKategori': slug
    })
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('search', views.search, name="search"),
    path('<slug:slug>', views.details, name='courses_details'),
    path('kategori/<slug:slug>', views.getCoursesByCategory, name='courses_by_category'),
]

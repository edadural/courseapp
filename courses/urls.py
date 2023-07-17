from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('<slug:slug>', views.details, name='courses_details'),  # veri tipi: slug
    path('kategori/<slug:slug>', views.getCoursesByCategory, name='courses_by_category'),
]

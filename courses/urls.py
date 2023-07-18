from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('search', views.search, name="search"),
    path('create-course', views.create_course, name="create_course"),
    path('course-list', views.course_list, name="course_list"),
    path('course-edit/<int:id>', views.course_edit, name="course_edit"),
    path('course-delete/<int:id>', views.course_delete, name="course_delete"),
    path('<slug:slug>', views.details, name='courses_details'),
    path('kategori/<slug:slug>', views.getCoursesByCategory, name='courses_by_category'),
]

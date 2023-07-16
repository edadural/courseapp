from django.contrib import admin
from .models import Course, Category

# Register your models here.

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ("title","isActive","slug",)
    list_display_links = ("title","slug",)
    readonly_fields = ("slug",)
    list_filter = ("title","isActive")
    list_editable = ("isActive",)
    search_fields = ("title","description",)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass
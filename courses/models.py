from django.db import models
from django.utils.text import slugify

class Course(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    imageUrl = models.CharField(max_length=50, blank=False)
    date = models.DateField()
    isActive = models.BooleanField()
    slug = models.SlugField(default="", null=False, unique=True, db_index=True)  # varolan kayıtlar için "", zorunlu alan false, unique benzersiz, db primary key icin aktif edilmesi

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)  # url parametresini duzgun bi sekilde olusturur
        super().save(args, kwargs)

    def __str__(self):
        return f"{self.title} {self.date}"
    
class Category(models.Model):
    name = models.CharField(max_length=40)
    slug = models.CharField(max_length=50)
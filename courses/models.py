from django.db import models
from django.utils.text import slugify
    
class Category(models.Model):
    name = models.CharField(max_length=40)
    slug = models.SlugField(default="", null=False, unique=True, db_index=True, max_length=50)

    def __str__(self):
        return f"{self.name}"
    
class Course(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    imageUrl = models.CharField(max_length=50, blank=False)
    date = models.DateField(auto_now=True)
    isActive = models.BooleanField()
    slug = models.SlugField(default="", blank=True, null=False, unique=True, db_index=True)  # varolan kayıtlar için "", blank ilgili formda bos deger girmek, formdaki slug bilgisi editlenmesin, zorunlu alan false, unique benzersiz, db primary key icin aktif edilmesi
    category = models.ForeignKey(Category, default=1, on_delete=models.CASCADE, related_name="kurslar")  # cascade: bir kategori silindigi zaman ona ait olan kurslar da silinir

    def __str__(self):
        return f"{self.title}"
from django.db import models
from django.utils.text import slugify
from ckeditor.fields import RichTextField
    
class Category(models.Model):
    name = models.CharField(max_length=40)
    slug = models.SlugField(default="", null=False, unique=True, db_index=True, max_length=50)

    def __str__(self):
        return f"{self.name}"
    
class Course(models.Model):
    title = models.CharField(max_length=50)
    subtitle =models.CharField(max_length=100, default="")
    description = RichTextField()
    image = models.ImageField(upload_to="images", default="")
    date = models.DateField(auto_now=True)
    isActive = models.BooleanField(default=False)
    isHome = models.BooleanField(default=False)
    slug = models.SlugField(default="", blank=True, null=False, unique=True, db_index=True)  # varolan kayıtlar için "", blank ilgili formda bos deger girmek, formdaki slug bilgisi editlenmesin, zorunlu alan false, unique benzersiz, db primary key icin aktif edilmesi
    categories = models.ManyToManyField(Category)

    def __str__(self):
        return f"{self.title}"
    
class Slider(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to="images")
    is_active = models.BooleanField(default=False)
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.title}"
    
class UploadModel(models.Model):
    image = models.ImageField(upload_to="images")  # upload_to parametresine verilen klasor altına dosyayı eklicek, konumuyla birlikte dosya bilgisini veritabanına model üzerinden kayıt etmek
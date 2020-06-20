from django.db import models
from ckeditor.fields import RichTextField
from django.utils.timezone import now


# Create your models here.
# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nombre")
    description = RichTextField(verbose_name="Descripción de la categoria")
    image = models.ImageField(verbose_name="Imagen de la categoria", upload_to="services")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "categoría"
        verbose_name_plural = "categorías"
        ordering = ['-created']
    
    

    def __str__(self):
        return self.name


class Subcategory(models.Model):
    categories = models.ForeignKey(Category, verbose_name="Categorías", related_name="get_categories", on_delete=models.CASCADE)
    description = RichTextField(verbose_name="Descripción de la categoria")
    image = models.ImageField(verbose_name="Imagen de la categoria", upload_to="services")
    name = models.CharField(max_length=100, verbose_name="Nombre")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "sub categoría"
        verbose_name_plural = "sub categorías"
        ordering = ['-created']
    
    

    def __str__(self):
        return self.name


class Service(models.Model):
    subcategories = models.ForeignKey(Subcategory, verbose_name="Sub categorías", related_name="get_services",on_delete=models.CASCADE)
    title = models.CharField(max_length=200, verbose_name="Título")
    subtitle = models.CharField(max_length=200, verbose_name="Subtítulo")
    content = RichTextField(verbose_name="Contenido")
    published = models.DateTimeField(verbose_name="Fecha de publicación", default=now)
    image = models.ImageField(verbose_name="Imagen", upload_to="services")
    brochure = models.FileField(verbose_name="Brochure", upload_to="services")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "servicio"
        verbose_name_plural = "servicios"
        ordering = ['-created']

    def __str__(self):
        return self.title
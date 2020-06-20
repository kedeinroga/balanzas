from django.db import models
from django.utils.timezone import now
from ckeditor.fields import RichTextField

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nombre")
    description = RichTextField(verbose_name="Descripción de la categoria")
    image = models.ImageField(verbose_name="Imagen de la categoria", upload_to="product")
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
    name = models.CharField(max_length=100, verbose_name="Nombre")
    description = RichTextField(verbose_name="Descripción de la subcategoria")
    image = models.ImageField(verbose_name="Imagen de la subcategoria", upload_to="product")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "subcategoría"
        verbose_name_plural = "subcategorías"
        ordering = ['-created']
    
    

    def __str__(self):
        return self.name

class Aplicaciones(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nombre")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "Aplicaciones"
        verbose_name_plural = "Lista de aplicaciones"
        ordering = ['-created']
    
    

    def __str__(self):
        return self.name

class Subaplicaciones(models.Model):
    listaplications = models.ForeignKey(Aplicaciones, verbose_name="Lista de aplicaciones", related_name="get_aplications",on_delete=models.CASCADE)
    name = models.CharField(max_length=100, verbose_name="Nombre")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "Subaplicaciones"
        verbose_name_plural = "Sub lista de aplicaciones"
        ordering = ['-created']
    
    

    def __str__(self):
        return self.name

class Product(models.Model):
    subcategories = models.ForeignKey(Subcategory, verbose_name="Sub categorías", related_name="get_products",on_delete=models.CASCADE)
    title = models.CharField(verbose_name="Título", max_length=200)
    description = models.CharField(verbose_name="Descripcion del producto", max_length=200)
    content = RichTextField(verbose_name="Contenido")
    codigo = models.CharField(verbose_name="Código", max_length=20, unique=True)
    precio = models.FloatField(verbose_name="Precio", default=0)
    peso = models.FloatField(verbose_name="Peso en Kg", default=0)
    volumen = models.FloatField(verbose_name="Volumen en m3", default=0)
    numparte = models.CharField(verbose_name="Número de parte", max_length=50, unique=True)
    image1 = models.ImageField(verbose_name="Imagen principal", upload_to="product")
    image2 = models.ImageField(verbose_name="Imagen secundaria", upload_to="product")
    image3 = models.ImageField(verbose_name="Imagen secundaria 2", upload_to="product")
    videourl = models.URLField(verbose_name="Video",max_length = 200, blank=True)
    hojadatos = models.FileField(verbose_name="Hoja de datos", upload_to="product")
    subaplications = models.ManyToManyField(Subaplicaciones, verbose_name="Sub lista de aplicaciones", related_name="get_subaplications")
    published = models.DateTimeField(verbose_name="Fecha de publicación", default=now)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "producto"
        verbose_name_plural = "productos"
        unique_together = ('codigo','numparte')
        ordering = ['-created']

    def __str__(self):
        return self.title

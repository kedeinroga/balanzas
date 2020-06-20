from django.contrib import admin

from .models import Category, Subcategory, Product, Aplicaciones, Subaplicaciones

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

class SubcategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

class AplicacionesAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

class SubaplicacionesAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

class ProductAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('title', 'published','codigo', 'precio', 'subcategories')
    ordering = ('title','published')
    search_fields = ('title','content', 'subcategories__name')
    date_hierarchy = 'published'
    list_filter = ('title','subcategories__name')

    class Media:
        css = {
            'all': ('core/css/custom_ckeditor.css',)
        }

    def product_categories(self, obj):
        return ", ".join([c.name for c in obj.categories.all().order_by("name")])
    product_categories.short_description = "Categorías"

admin.site.register(Aplicaciones, AplicacionesAdmin)
admin.site.register(Subaplicaciones, SubaplicacionesAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Subcategory, SubcategoryAdmin)
admin.site.register(Product, ProductAdmin)

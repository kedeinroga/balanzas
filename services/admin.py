from django.contrib import admin
from .models import Service, Category, Subcategory

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

class SubcategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')


class ServiceAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('title', 'published', 'subcategories')
    ordering = ('title','published')
    search_fields = ('title','content', 'subcategories__name')
    date_hierarchy = 'published'
    list_filter = ('title','subcategories__name')

    class Media:
        css = {
            'all': ('core/css/custom_ckeditor.css',)
        }

    

admin.site.register(Category, CategoryAdmin)
admin.site.register(Subcategory, SubcategoryAdmin)
admin.site.register(Service, ServiceAdmin)
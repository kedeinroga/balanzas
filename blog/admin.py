from django.contrib import admin
#from mptt.admin import MPTTModelAdmin,DraggableMPTTAdmin
from .models import Category, Post

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

class PostAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('title', 'author', 'published', 'post_categories')
    ordering = ('author', 'published')
    search_fields = ('title','content','author__username', 'categories__name')
    date_hierarchy = 'published'
    list_filter = ('author__username','categories__name')

    class Media:
        css = {
            'all': ('core/css/custom_ckeditor.css',)
        }

    def post_categories(self, obj):
        return ", ".join([c.name for c in obj.categories.all().order_by("name")])
    post_categories.short_description = "Categorías"

admin.site.register(Category, CategoryAdmin)
#admin.site.register(Category, MPTTModelAdmin)
admin.site.register(Post, PostAdmin)

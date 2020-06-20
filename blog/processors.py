from .models import Category
from django import template


def ctx_dict(request):
    return {'post_context':Category.objects.order_by('name')} 


#def ctx_dict(request):
    #ctx = {}
    #categories = Category.objects.all()
    #for category in categories:
        #ctx[category.name] = category.name
        #ctx[category.id] = category.id
        #print(ctx)
    #return ctx


#def ctx_dict(request):
    #ctx = {}
    #categories = Category.objects.all()
    #for category in categories:
        #ctx[blog_patterns] = blog_patterns.category
        #print(ctx)
    #return ctx


#register = template.Library()

#@register.simple_tag
#def ctx_dict(request):
    #category = Category.objects.all()
    #return category
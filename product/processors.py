from .models import Category, Subcategory, Product
from django import template


def ctx_dict(request):
    prod_context = Product.objects.order_by('name')
    cat_context = Category.objects.order_by('name')
    sub_context = Subcategory.objects.order_by('name')
    product_context = {'pcat_context':cat_context, 'psub_context':sub_context, 'pprod_context':prod_context}
    #prod_context = Product.objects.values('title')
    #print(product_context)
    return product_context  #MainMenu.objects.all().select_related().order_with_respect_to('name')
    #return {'product_context':Category.objects.select_related().order_with_respect_to('name')}


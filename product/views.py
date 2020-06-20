from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Product, Category, Subcategory, Aplicaciones
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.

class ProductListView(ListView):
    model = Product
    template_name = 'product/product_list.html'
    paginate_by = 6
    
    

class ProductDetailView(DetailView):
    model = Product
    template_name = 'product/product_detail.html'

class CategoryDetailView(DetailView):
    model = Category
    template_name = 'product/category_detail.html'
    paginate_by = 6

class SubcategoryDetailView(DetailView):
    model = Subcategory
    template_name = 'product/subcategory_detail.html'
    paginate_by = 6
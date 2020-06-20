from django.shortcuts import render
from .models import Service, Category, Subcategory
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.http import HttpResponse, HttpResponseRedirect
from django.db.models import Q
# Create your views here.

class ServicesListView(ListView):
    model = Service
    template_name = 'services/service_list.html'
    paginate_by = 6


class ServicesDetailView(DetailView):
    model = Service


class CategoryDetailView(DetailView):
    model = Category
    template_name = 'services/category_detail.html'
    paginate_by = 6

class SubcategoryDetailView(DetailView):
    model = Subcategory
    template_name = 'services/subcategory_detail.html'
    paginate_by = 6
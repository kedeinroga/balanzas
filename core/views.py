from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect


from blog.models import Post, Category

# Create your views here.

def home(request):
    category = Category.objects.all()
    context = {'category':category}
    return render(request, "core/home.html",context)

def about(request):
    return render(request, "core/about.html")

def store(request):
    return render(request, "core/store.html")


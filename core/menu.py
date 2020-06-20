from django.shortcuts import render

# Create your views here.
from django.views.generic.list import ListView

from blog.models import Post

class MenuListView(ListView):

    model = Post
    template_name = 'core/menu.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        return context

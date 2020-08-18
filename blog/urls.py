from django.urls import path
from .views import BlogListView, BlogDetailView, CategoryDetailView, SearchView

blog_patterns = ([
    path('', BlogListView.as_view(), name='blog'),
    path('<int:pk>/<slug:slug>/', BlogDetailView.as_view(), name='detail'),
    path('category/<int:pk>/<slug:slug>/', CategoryDetailView.as_view(), name='category'),
    path('search/', SearchView.as_view(), name='search'),
], 'blog')
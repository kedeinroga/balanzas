from django.urls import path
from .views import ProductListView, ProductDetailView, CategoryDetailView, SubcategoryDetailView

product_patterns = ([
    path('', ProductListView.as_view(), name='products'),
    path('<int:pk>/<slug:slug>/', ProductDetailView.as_view(), name='detail'),
    path('category/<int:pk>/<slug:slug>/', CategoryDetailView.as_view(), name='category'),
    path('subcategory/<int:pk>/<slug:slug>/', SubcategoryDetailView.as_view(), name='subcategory'),
], 'product')
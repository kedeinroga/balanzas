from .models import Category, Subcategory, Service
from django import template


def ctx_dict(request):
    sser_context = Service.objects.order_by('name')
    scat_context = Category.objects.order_by('name')
    ssub_context = Subcategory.objects.order_by('name')
    services_context = {'scat_context':scat_context, 'ssub_context':ssub_context, 'sser_context':sser_context}
    return services_context


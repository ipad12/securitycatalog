from django.shortcuts import render, HttpResponse
from django.template import loader

from .models import Domain, Technology, Product

def index(request):
    
    domain_list = Domain.objects.order_by('name')
    technology_list = Technology.objects.order_by('name')
    product_list = Product.objects.order_by('name')
    context = {
        'domain_list' : domain_list,
        'technology_list' : technology_list,
        'product_list' : product_list,
    }
    
    return render(request, 'security/index.html', context)
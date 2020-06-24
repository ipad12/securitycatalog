from django.shortcuts import get_object_or_404, render, HttpResponse
from django.template import loader
from django.contrib import admin
from django.contrib.admin.models import LogEntry
from django.contrib.auth import logout


from .models import Domain, Technology, Product, ProdSlideDeck, ScopeDoc, POCSOW, Datasheet, CompetitiveInfo


def home(request):
    
    logentry_list = LogEntry.objects.order_by('-action_time')
    domain_list = Domain.objects.order_by('name')
    technology_list = Technology.objects.order_by('name')
    product_list = Product.objects.order_by('name')
    context = {
        'domain_list' : domain_list,
        'technology_list' : technology_list,
        'product_list' : product_list,
        'logentry_list' : logentry_list,
    }
    
    return render(request, 'security/homepage.html', context)

def techlist(request, domain_id, technology_id):
    
    technology = get_object_or_404(Technology, pk=technology_id)
    domain_list = Domain.objects.order_by('name')
    technology_list = Technology.objects.order_by('name')
    product_list = Product.objects.order_by('name')
    context = {
        'domain_list' : domain_list,
        'technology_list' : technology_list,
        'product_list' : product_list,
        'Technology' : technology,
    }
    
    return render(request, 'security/techlist.html', context)

def productview(request, domain_id, technology_id, product_id):
    
    technology = get_object_or_404(Technology, pk=technology_id)
    product = get_object_or_404(Product, pk=product_id)
    prodslidedeck_list = ProdSlideDeck.objects.order_by('name')
    scopedoc_list = ScopeDoc.objects.order_by('name')
    pocsow_list = POCSOW.objects.order_by('name')
    datasheet_list = Datasheet.objects.order_by('name')
    competitiveinfo_list = CompetitiveInfo.objects.order_by('name')
    domain_list = Domain.objects.order_by('name')
    technology_list = Technology.objects.order_by('name')
    product_list = Product.objects.order_by('name')
    context = {
        'domain_list' : domain_list,
        'technology_list' : technology_list,
        'product_list' : product_list,
        'Technology' : technology,
        'Product' : product,
        'prodslidedeck_list': prodslidedeck_list,
        'scopedoc_list' : scopedoc_list,
        'pocsow_list' : pocsow_list,
        'datasheet_list' : datasheet_list,
        'competitiveinfo_list' : competitiveinfo_list,
        }
    
    return render(request, 'security/productview.html', context)
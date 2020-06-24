from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

app_name = 'security'

urlpatterns = [
    path('', views.home, name='home'),
    path('<int:domain_id>/<int:technology_id>/', views.techlist, name='tech list'),
    path('<int:domain_id>/<int:technology_id>/<int:product_id>/', views.productview, name='product view'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
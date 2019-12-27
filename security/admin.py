from django.contrib import admin

from .models import Domain, Technology, Product

admin.site.register(Domain)
admin.site.register(Technology)
admin.site.register(Product)


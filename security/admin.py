from django.contrib import admin

from .models import Domain, Technology, Product, ProdSlideDeck, ScopeDoc, POCSOW, Datasheet, CompetitiveInfo, Vendor


from django.contrib.admin.models import LogEntry

class PSDInLine(admin.StackedInline):
    model = ProdSlideDeck
    extra=0
    
class SDInLine(admin.StackedInline):
    model = ScopeDoc
    extra=0
    
class POCSOWInLine(admin.StackedInline):
    model = POCSOW
    extra=0
    
class DSInLine(admin.StackedInline):
    model = Datasheet
    extra=0
    
class CIInLine(admin.StackedInline):
    model = CompetitiveInfo
    extra=0
    
class ProductAdmin(admin.ModelAdmin):    
    inlines = [
        PSDInLine,
        SDInLine,
        POCSOWInLine,
        DSInLine,
        CIInLine,
    ]
    save_on_top=True
    list_display = ('name','vendor', 'technologies')
    list_filter = ['vendor']
    filter_horizontal = ['technology']
    
    def technologies(self, product):
        return ",\n".join([p.name for p in product.technology.all()])
    
class TechnologyAdmin(admin.ModelAdmin):
    list_display = ('name', 'domain', 'description')
    list_filter = ['domain']
    
class DomainAdmin(admin.ModelAdmin):
    list_display = ('name', '_id')

class LogEntryAdmin(admin.ModelAdmin):
    readonly_fields = ('content_type',
        'user',
        'action_time',
        'object_id',
        'object_repr',
        'action_flag',
        'change_message'
    )

    def has_delete_permission(self, request, obj=None):
        return False

    def get_actions(self, request):
        actions = super(LogEntryAdmin, self).get_actions(request)
        del actions['delete_selected']
        return actions

admin.site.register(LogEntry, LogEntryAdmin)
admin.site.register(Technology, TechnologyAdmin)    
admin.site.register(Product, ProductAdmin)
admin.site.register(Domain, DomainAdmin)
admin.site.register(Vendor)
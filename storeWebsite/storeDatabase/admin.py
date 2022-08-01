from django.contrib import admin
from .models import CustomerCompany, Supplier, StoreItem, WebsiteInfo, RecipesItem


class CustomerCompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'discountForCompany')
    search_fields = ('name', 'discountForCompany')


class SupplierAdmin(admin.ModelAdmin):
    list_display = ('name', 'display_store_items')
    search_fields = ('name', 'display_store_items')


class StoreItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'show', 'created_at', 'updated_at')
    list_filter = ('supplier',)
    list_editable = ('show',)
    search_fields = ('name',)


class RecipesItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'show', 'get_related_products', 'created_at', 'updated_at')
    list_editable = ('show',)
    search_fields = ('name','get_related_products', 'show')


admin.site.register(CustomerCompany, CustomerCompanyAdmin)
admin.site.register(Supplier, SupplierAdmin)
admin.site.register(StoreItem, StoreItemAdmin)
admin.site.register(RecipesItem, RecipesItemAdmin)
admin.site.register(WebsiteInfo)

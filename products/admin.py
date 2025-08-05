from django.contrib import admin
from .models import *


# Custom Admins
class ItemAdmin(admin.ModelAdmin):
    list_display = ['item_name','item_price','created_at']
    search_fields = ['name']



# Register your models here.
admin.site.register(Item,ItemAdmin)

# products/admin.py




@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'category')
    search_fields = ('name', 'category')
    list_filter = ('category',)

from django.contrib import admin
from . models import Product,Order,Category

admin.site.site_header="My Inventory Dashboard"

class ProductAdmin(admin.ModelAdmin):
    list_display=('name','category','quantity')
    #list_display=('name','Category','quantity')
    list_filter=['category']
    #list_filter=['Category']
    list_editable=['quantity']
# Register your models here.
#admin.site.register(Product)
admin.site.register(Product,ProductAdmin)
admin.site.register(Order)
admin.site.register(Category)

from django.contrib import admin
from productApp.models import Category,Product

from import_export import resources 
from import_export.admin import ImportExportMixin
# Register your models here

class productResource(resources.ModelResource):
    class Meta:
        model = Product
        exclude = ('images',)


class productAdmin(ImportExportMixin,admin.ModelAdmin):
    list_display=["id","product_name", "description", "Category",  "totalprice"]
    list_filter = ["Category"]
    search_fields = [ "product_name", "description"]
    prepopulated_fields={"slug":("product_name",)}

    resource_class = productResource
    perpopulated_feilds = {"slug":("product_name",)}

admin.site.register(Product, productAdmin)
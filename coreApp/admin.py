from itertools import product
from django.contrib import admin
from categoryApp.models import Category

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):

    prepopulated_fields={"slug": ("category_name",)}

    class Meta:
        model= product

admin.site.register(Category,CategoryAdmin)


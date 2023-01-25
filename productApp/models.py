
from django.db import models
from django.utils.text import slugify

from categoryApp.models import Category

from django.core.exceptions import ValidationError

# Create your models here.
class Product(models.Model):
    product_name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True,blank=True)
    description= models.TextField(max_length=500, blank=True)
    unitprice= models.IntegerField()
    quantity=models.IntegerField()
    totalprice=models.IntegerField(null=True,blank=True,default=0)
    images=models.FileField(upload_to='photos/products',default='photos/products/blank.png',blank=True)
    Category= models.ForeignKey(Category, on_delete=models.CASCADE)
    created_date=models.DateTimeField(auto_now_add=True)
    modified_date=models.DateTimeField(auto_now=True)

    def __str__(self):
        return"%s-%s-%s" %(self.id,self.product_name,self.quantity)

    def save(self, *args, **kwargs):
        self.slug= slugify(self.product_name)
        self.totalprice= self.unitprice *self.quantity
        super(Product, self).save(*args, **kwargs)

    def delete(self,using=None, Keep_parents=False):
        print(self.images.name)
        if self.images.name != "photos/products/blank.png":
            self.images.storage.delete(self.images.name)
        super().delete()
    def clean(self):
        if self.quantity < 1:
            raise ValidationError(
                {
                    "quantity": "Quantity Cannot Less Than 1"
                }
            )
        super(Product,self).clean()
    

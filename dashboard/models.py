from django.db import models
from django.contrib.auth.models import User
from mptt.models import MPTTModel, TreeForeignKey
from mptt.admin import DraggableMPTTAdmin

# Create your models here.
#CATEGORY = (
#    ('Stationary', 'Stationary'),
#    ('Electronics', 'Electronics'),
#    ('Food', 'Food'),
#)

#class Category(models.Model):
class Category(MPTTModel):
    category = models.CharField(max_length=50,  null=True)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')    

    #class Meta:
    #    verbose_name_plural="Category"

    class MPTTMeta:
        order_insertion_by = ['category']

    def __str__(self):
        return f'{self.category}'


class Product(models.Model):
    name = models.CharField(max_length=100, null=True)
    quantity = models.PositiveIntegerField(null=True)
    category = models.ForeignKey(Category,on_delete=models.CASCADE,null=True)
    #category = models.CharField(max_length=50, null=True)
    #category = models.CharField(max_length=50, choices=CATEGORY, null=True)


    class Meta:
        verbose_name_plural="Product"

    def __str__(self):
        return f'{self.name}-{self.quantity}'

class Order(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE,null=True)
    staff=models.ForeignKey(User,models.CASCADE,null=True)
    order_quantity=models.PositiveIntegerField(null=True)
    data=models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name_plural="Order"

    def __str__(self):
        return f'{self.product} ordered by {self.staff.username}'


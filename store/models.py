from distutils.command.upload import upload
from pydoc import describe
from unicodedata import category
from django.db import models
from category.models import Category
from django.urls import reverse

# Create your models here.

class Product(models.Model):
    product_name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    describetion = models.TextField(max_length=500, blank=True)
    images = models.ImageField(upload_to='photos/products/')
    price = models.IntegerField(default=0)
    stoke = models.IntegerField()
    is_available = models.BooleanField(default=True)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    create_date = models.DateTimeField(auto_now_add=True)
    modifield_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product_name

    def get_url(self):
        return reverse('product_detail',args=[self.category.slug, self.slug])


from tabnanny import verbose
from django.db import models
from django.urls import reverse

# Create your models here.

class Category(models.Model):
    category_name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=50, unique=True)
    describtion = models.TextField(max_length=300, blank =True)
    cate_image = models.ImageField(upload_to='photos/categories/')

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
    
    def get_url(self):
        return reverse('product_by_category',args=[self.slug])

    def __str__(self):
        return self.category_name


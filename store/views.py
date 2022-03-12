from django.shortcuts import get_object_or_404, render
from store.models import Product
from category.models import Category
# Create your views here.
def store(request,category_slug=None):
    categories = None #this field is not mendatory
    products = None #this field is not mendatory
    if category_slug !=None:
        categories = get_object_or_404(Category, slug=category_slug) #this slug=category_slug here slug is reference in category model field is not mendatory
        products = Product.objects.filter(category=categories, is_available=True)
        product_count = products.count()
    else:    
        products = Product.objects.all().filter(is_available=True)
        product_count = products.count()
    cotnext ={
        'products': products,
        'product_count': product_count
    }
    return render(request,'store/store.html',cotnext)


from unicodedata import name
from django.urls import path
from store import views

urlpatterns = [
    path('',views.store, name='store'),
    path('<slug:category_slug>/',views.store, name='product_by_category'),
]


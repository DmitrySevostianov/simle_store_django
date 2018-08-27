from django.shortcuts import render

from django.views.generic import ListView, DetailView


from .models import Product


class ProductList(ListView):
    model = Product
    context_object_name = 'product_list'

class ProductDetail(DetailView):
    model = Product
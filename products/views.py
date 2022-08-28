from django.shortcuts import render, get_list_or_404
from .models import Product

def all(request):
    # products = Product.get_object_or_404.all()
    products = get_list_or_404(Product)

    context = {
        'products': products,
    }
    return render(request, 'products/all.html', context)

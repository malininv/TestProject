from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import Product, Category


def index(request):
    products = Product.objects.all()
    categories = Category.objects.all()
    context = {
        'products': products,
        'categories': categories,
    }

    template = 'testpr/index.html'

    return render(request, template, context)


# def products_by_category(request, category_slug):
#     products = Product.objects.filter(product_category=category_slug)
#     categories = Category.objects.filter(parent__isnull=True)
#     slug = category_slug
#
#     if slug:
#         category_s = get_object_or_404(Category, slug=slug)
#         products = products.filter(category=category_s)
#
#     context = {
#         'products': products,
#         'categories': categories,
#         'category': category_s
#     }
#
#     template = 'templates/index.html'
#
#     return render(request, template, context)

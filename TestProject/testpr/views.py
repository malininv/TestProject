from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import Product, Category


def index(request):
    products = Product.objects.all()
    categories = Category.objects.filter(parent__isnull=True)
    context = {
        'products': products,
        'categories': categories,
    }

    template = 'testpr/index.html'

    return render(request, template, context)


def products_by_category(request, category_slug):
    slug = category_slug
    category = Category.objects.filter(slug=slug)

    subcategories = Category.objects.filter(parent__in=category)

    if slug:
        category_s = get_object_or_404(Category, slug=slug)
        products = Product.objects.filter(category=category_s)

    context = {
        'products': products,
        'category': category,
        'subcategories': subcategories
    }

    template = 'testpr/by_category.html'

    return render(request, template, context)

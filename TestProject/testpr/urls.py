from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<str:category_slug>/', views.products_by_category, name='product-categories')
]
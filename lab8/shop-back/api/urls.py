from django.urls import path
from . import views

urlpatterns = [
    # Маршруты для продуктов
    path('products/', views.product_list),
    path('products/<int:id>/', views.product_detail),
    
    # Маршруты для категорий
    path('categories/', views.category_list),
    path('categories/<int:id>/', views.category_detail),
    path('categories/<int:id>/products/', views.category_products),
]
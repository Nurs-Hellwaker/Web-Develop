from django.contrib import admin
from .models import Category, Product

# Регистрируем наши модели, чтобы они появились в админке
admin.site.register(Category)
admin.site.register(Product)
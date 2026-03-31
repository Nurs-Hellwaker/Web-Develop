from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),   # <--- Вот эта строка включает админку!
    path('api/', include('api.urls')), # Это наше приложение api
]
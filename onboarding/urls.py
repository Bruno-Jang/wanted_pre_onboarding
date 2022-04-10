from django.urls import path, include

urlpatterns = [
    path('products', include('products.urls')),
    path('members', include('members.urls')),
]

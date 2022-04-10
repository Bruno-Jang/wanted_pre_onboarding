from django.urls import path

from products.views import ProductCreationView, ProductDeletionView, ProductDetailView

urlpatterns = [
    path('/openfunding', ProductCreationView.as_view()),
    path('/<int:product_id>/publisher/<int:publisher_id>', ProductDeletionView.as_view()),
    path('/<int:product_id>', ProductDetailView.as_view()),
]

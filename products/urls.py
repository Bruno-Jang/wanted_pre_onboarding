from django.urls import path

from products.views import ProductCreationView, ProductDeletionView

urlpatterns = [
    path('/openfunding', ProductCreationView.as_view()),
    path('/<int:product_id>/publisher/<int:publisher_id>', ProductDeletionView.as_view()),
]

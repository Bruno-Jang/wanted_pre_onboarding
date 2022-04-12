from django.urls import path

from products.views import ProductCreationView, ProductDeletionView, ProductDetailView, ProductListView, ProductUpdateView

urlpatterns = [
    path('/openfunding', ProductCreationView.as_view()),
    path('/<int:product_id>/publisher/<int:publisher_id>', ProductDeletionView.as_view()),
    path('/<int:product_id>', ProductDetailView.as_view()),
    path('/list', ProductListView.as_view()),
    path('/<int:product_id>', ProductUpdateView.as_view()),
]

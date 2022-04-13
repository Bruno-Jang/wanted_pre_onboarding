from django.urls import path

from products.views import ProductCreationView, ProductDetailView, ProductListView, ProductManageView

urlpatterns = [
    path('/openfunding', ProductCreationView.as_view()),
    path('/<int:product_id>', ProductManageView.as_view()),
    path('/detail/<int:product_id>', ProductDetailView.as_view()),
    path('/list', ProductListView.as_view()),
]

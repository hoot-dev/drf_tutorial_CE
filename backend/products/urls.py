from django.urls import path

from .views import (
    ProductDetailAPIView, ProductListCreateAPIView, product_alt_view
)

urlpatterns = [
    path('', product_alt_view),
    path('<int:pk>/', product_alt_view)
]
from rest_framework import mixins, viewsets

from .models import Product
from .serializers import ProductSerializer


class ProductViewSet(viewsets.ModelViewSet):
    """
    get -> list -> Queryset
    get -> retrieve -> Product instance detail view
    post -> create -> New instance
    put -> update
    patch -> partial update
    delete -> destroy
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_fields = 'pk' # default

class ProductGenericViewSet(
        mixins.ListModelMixin,
        mixins.RetrieveModelMixin,
        viewsets.GenericViewSet):
    """
    get -> list -> Queryset
    get -> retrieve -> Product instance detail view
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_fields = 'pk' # default
from rest_framework import viewsets
from .models import *
from .serializers import *

class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

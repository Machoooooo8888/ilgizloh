from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import CreateAPIView
from .serializers import *
from .models import *


class CategoryView(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class ProductView(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_serializer_class(self):
        if self.action == 'list':
            return ProductListSerializer
        return self.serializer_class

class ProductImageView(CreateAPIView):
    queryset = ProductImage.objects.all()
    serializer_class = ProductImageSerializer

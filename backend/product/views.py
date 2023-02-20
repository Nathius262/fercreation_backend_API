from rest_framework import mixins, generics
from rest_framework.response import Response
from rest_framework import status
from .serializers import ProductSerializers, CategorySerializers
from .models import Product, Category
from .utils import SetProductPaginationResult

class CategoryViewSet(generics.GenericAPIView, mixins.ListModelMixin):
    serializer_class = CategorySerializers
    queryset = Category.objects.all()
    lookup_field = 'category_name'

    def get(self, request, category_name=None):
        return self.list(request)
        

class ProductViewSet(generics.GenericAPIView, mixins.RetrieveModelMixin, mixins.ListModelMixin):
    serializer_class = ProductSerializers
    queryset = Product.objects.all()
    lookup_field = 'slug'
    #pagination_class = [SetProductPaginationResult]

    def get(self, request, slug=None):
        if slug:
            return self.retrieve(request)
        else:
            return self.list(request)
        
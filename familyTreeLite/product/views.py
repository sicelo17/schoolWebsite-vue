from django.http import Http404

from rest_framework.views import APIView
from rest_framework.response import Response 

from .models import Product
from .serializers import ProductSerializer

class LatestProductsList(APIView):
    def get(self, request, format=None):
        products = Product.objects.all()[0:4]  #getting the first four items from the database
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)


class ProductDetail(APIView):
    def get_object(self, category_slug, product_slug):
        try:
            return Product.objects.filter(category__slug=category_slug).get(slug=product_slug)
        except Product.DoesNotExist:
            raise Http404

    def get(self, request, category_slug, product_slug, format=None):
        product = self.get_object(category_slug, product_slug)
        serializer = ProductSerializer(product)     #getting data from serializers.py
        return Response(serializer.data)


class CategoryDetail(APIView):
    def get_object(self, category_slug):
        try: 
            return Category.objects.get(slug=category_slug)
        except Product.DoesNotExist:
            raise Http404

    def get(self, request, category_slug, format=None):
        product = self.get_object(category_slug)
        serializer = CategorySerializer(category)     #getting data from serializers.py
        return Response(serializer.data)
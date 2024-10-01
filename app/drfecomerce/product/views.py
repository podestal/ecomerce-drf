from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from drf_spectacular.utils import extend_schema

from . import models
from . import serializers


class CategoryViewSet(viewsets.ViewSet):
    """
    A simple viewset for viewing all the categories
    """

    queryset = models.Category.objects.all()

    @extend_schema(responses=serializers.CategorySerializer)
    def list(self, request):
        serializer = serializers.CategorySerializer(self.queryset, many=True)
        return Response(serializer.data)


class BrandViewSet(viewsets.ViewSet):
    """
    A simple viewset for viewing all the brands
    """

    queryset = models.Brand.objects.all()

    @extend_schema(responses=serializers.BrandSerializer)
    def list(self, request):
        serializer = serializers.BrandSerializer(self.queryset, many=True)
        return Response(serializer.data)


class ProductViewSet(viewsets.ViewSet):
    """
    A simple viewset for viewing all the products
    """

    queryset = models.Product.objects.select_related("category", "brand")
    lookup_field = "slug"

    def retrieve(self, request, slug=None):
        serializer = serializers.ProductSerializer(
            self.queryset.filter(slug=slug), many=True
        )
        return Response(serializer.data)

    @extend_schema(responses=serializers.ProductSerializer)
    def list(self, request):
        serializer = serializers.ProductSerializer(self.queryset, many=True)
        return Response(serializer.data)

    @action(
        methods=["get"],
        detail=False,
        url_path=r"category/(?P<category>\w+)/all",
        url_name="all",
    )
    def list_product_by_category(self, request, category=None):
        """
        An endpoint to return products by category
        """
        print("category param:", category)
        serializer = serializers.ProductSerializer(
            self.queryset.filter(category__name=category), many=True
        )
        return Response(serializer.data)

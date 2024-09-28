# from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
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

    queryset = models.Product.objects.all()

    @extend_schema(responses=serializers.ProductSerializer)
    def list(self, request):
        serializer = serializers.ProductSerializer(self.queryset, many=True)
        return Response(serializer.data)

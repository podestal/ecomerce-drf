from . import models
from rest_framework import serializers


class CategorySerializer(serializers.ModelSerializer):

    category_name = serializers.CharField(source="name")

    class Meta:
        model = models.Category
        fields = ["category_name"]


class BrandSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Brand
        fields = ["id", "name"]


class ProductLineSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Category
        fields = ["id", "sku", "stock_qty"]


class ProductSerializer(serializers.ModelSerializer):
    brand_name = serializers.CharField(source="brand.name")
    category = serializers.CharField(source="category.name")
    product_line = ProductLineSerializer(many=True)

    class Meta:
        model = models.Product
        fields = [
            "id",
            "name",
            "slug",
            "description",
            "category",
            "brand_name",
            "product_line",
        ]

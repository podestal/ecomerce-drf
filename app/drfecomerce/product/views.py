# from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response

from . import models
from . import serializers


class CategoryViewSet(viewsets.ViewSet):
    """
    A simple viewset for viewing all the categories
    """

    queryset = models.Category.objects.all()

    def list(self, request):
        serializer = serializers.CategorySerializer(self.queryset, many=True)
        return Response(serializer.data)

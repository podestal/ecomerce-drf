import factory

from drfecomerce.product import models


class CategoryFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = models.Category


class BrandFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = models.Brand


class ProductFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = models.Product

    category = factory.SubFactory(CategoryFactory)
    brand = factory.SubFactory(BrandFactory)

import factory

from drfecomerce.product import models


class CategoryFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = models.Category

    name = factory.sequence(lambda n: "Category_%d" % n)


class BrandFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = models.Brand

    name = factory.sequence(lambda n: "Brand%d" % n)


class ProductFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = models.Product

    category = factory.SubFactory(CategoryFactory)
    brand = factory.SubFactory(BrandFactory)

import factory

from drfecomerce.product import models


class CategoryFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = models.Category

    name = "test_category"

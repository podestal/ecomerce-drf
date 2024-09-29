import pytest
from pytest_factoryboy import register
from rest_framework.test import APIClient
from . import factories

register(factories.CategoryFactory)
register(factories.ProductFactory)
register(factories.BrandFactory)


@pytest.fixture
def api_client():
    return APIClient

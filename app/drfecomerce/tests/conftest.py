from pytest_factoryboy import register
from . import factories

register(factories.CategoryFactory)
register(factories.ProductFactory)
register(factories.BrandFactory)

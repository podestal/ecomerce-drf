from django.contrib import admin

from . import models


class ProductLineInLine(admin.TabularInline):
    model = models.ProductLine


@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductLineInLine]


admin.site.register(models.Category)
admin.site.register(models.Brand)
admin.site.register(models.ProductLine)

# Generated by Django 5.1.1 on 2024-09-29 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("product", "0002_alter_category_name"),
    ]

    operations = [
        migrations.AlterField(
            model_name="brand",
            name="name",
            field=models.CharField(max_length=100, unique=True),
        ),
    ]

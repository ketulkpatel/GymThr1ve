# Generated by Django 3.2.1 on 2021-05-07 07:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='product_price',
            field=models.CharField(default=10000, max_length=100),
            preserve_default=False,
        ),
    ]

from django.db import models
from account.models import *
# Create your models here.

class Brand(models.Model):
	brand_id=models.AutoField(primary_key=True)
	brand_name=models.CharField(max_length=100)

class Product(models.Model):
	product_id=models.AutoField(primary_key=True)
	product_name=models.CharField(max_length=100)
	product_price=models.CharField(max_length=100)
	product_qnt=models.IntegerField()
	brand_id=models.ForeignKey(Brand,related_name='brand',on_delete=models.CASCADE)


class Cart(models.Model):
	product_id=models.ForeignKey(Product,related_name='product',on_delete=models.CASCADE)
	product_qnt=models.IntegerField()
	product_price=models.IntegerField()
	product_status=models.BooleanField(default=True)
	user_id=models.ForeignKey(User,related_name='user',on_delete=models.CASCADE)
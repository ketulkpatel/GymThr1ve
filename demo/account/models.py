from django.db import models

# Create your models here.
class User(models.Model):
    user_id=models.AutoField(primary_key=True)
    u_name=models.CharField(max_length=100)
    u_password=models.CharField(max_length=100)
    email_id=models.CharField(max_length=100)
    mobile_num=models.CharField(max_length=10)
    alternate_mobile_num=models.CharField(max_length=10)


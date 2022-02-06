from django.db import models

# Create your models here.

class Customer(models.Model):
    Customer_id = models.AutoField(auto_created=True,primary_key=True)
    customer_username = models.CharField(max_length=25)
    customer_lname = models.CharField(max_length=25)
    email = models.CharField(max_length=25)
    password = models.CharField(max_length=25)
    confirm_password = models.CharField(max_length=25)


    class Meta:
        db_table = 'customer'
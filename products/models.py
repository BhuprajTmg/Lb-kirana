from django.db import models

# Create your models here.
class Products(models.Model):
    products_id= models.AutoField(auto_created=True,primary_key=True)
    products_name =models.CharField(max_length=200)
    products_price= models.CharField(max_length=100)

    class Meta:
        db_table="products"


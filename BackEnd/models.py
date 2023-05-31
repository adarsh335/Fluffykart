from django.db import models

# Create your models here.
class categoryDB(models.Model):
    CategoryName = models.CharField(max_length=50, null=True,blank=True)
    Description = models.CharField(max_length=100,null=True,blank=True)
    SubCategory = models.CharField(max_length=100, null=True, blank=True)
    CategoryImage = models.ImageField(upload_to="CatCategory",null=True,blank=True)
class productDB(models.Model):
    Category_Name = models.CharField(max_length=50, null=True, blank=True)
    Product_Name = models.CharField(max_length=50, null=True, blank=True)
    Quantity =models.IntegerField(max_length=100,null=True,blank=True)
    Description = models.CharField(max_length=100, null=True, blank=True)
    Price = models.IntegerField(max_length=100000, null=True, blank=True)
    Sub_Category = models.CharField(max_length=50, null=True, blank=True)
    Product_Image = models.ImageField(upload_to="ProductImg", null=True, blank=True)





from django.db import models

# Create your models here.
class messageDB(models.Model):
    Message = models.CharField(max_length=100, null=True, blank=True)
    SenderName = models.CharField(max_length=100, null=True, blank=True)
    Mail = models.EmailField(max_length=100, null=True, blank=True)
    Subject = models.CharField(max_length=100, null=True, blank=True)
class loginDB(models.Model):
    uNAME = models.CharField(max_length=10,null=True,blank=True)
    uPASS = models.CharField(max_length=16, blank=True,null=True)
class cartDB(models.Model):
    ProductName = models.CharField(max_length=100,null=True,blank=True)
    UserName= models.CharField(max_length=100,null=True,blank=True)
    Price = models.IntegerField(null=True, blank=True)
    Quantity = models.IntegerField(null=True, blank=True)
    ProductImage = models.ImageField(upload_to="ProductImage", null=True, blank=True)
    TotalPrice = models.IntegerField(null=True, blank=True)
class checkoutDB(models.Model):
    ProductName = models.CharField(max_length=100, null=True, blank=True)
    UserName = models.CharField(max_length=100, null=True, blank=True)
    Price = models.IntegerField(null=True, blank=True)
    Quantity = models.IntegerField(null=True, blank=True)
    PaymentMode = models.CharField(max_length=100, null=True, blank=True)
    TotalPrice = models.IntegerField(null=True, blank=True)
    Customer = models.CharField(max_length=100, null=True, blank=True)
    Address = models.CharField(max_length=100, null=True, blank=True)
    Phone = models.CharField(max_length=100,null=True, blank=True)
    Pincode = models.CharField(max_length=100,null=True, blank=True)









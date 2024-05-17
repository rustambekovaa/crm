from django.db import models


class Customer(models.Model):
    name = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    date_create = models.DateTimeField(auto_now_add = True,null=True)

    def __str__(self):
        return self.name
    

class Tag(models.Model):
    name = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name



class Product(models.Model):
    CATEGORY = (
        ('Indoor','Indoor'),
        ('Out Door','Out Door'),
    )
    name = models.CharField(max_length=200)
    price = models.IntegerField(max_length=200)
    category = models.CharField(max_length=200,null=True,choices=CATEGORY)
    description = models.DateTimeField(auto_now_add = True,null=True,blank=True)
    date_create = models.DateTimeField(auto_now_add = True,null=True)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.name


class Order(models.Model):
    STATUS = (
        ('Pending','Pending'),
        ('Out for deliver','Out for deliver'),
        ('Deliver','deliver')
    )
    customer = models.ForeignKey(Customer,null=True,on_delete = models.SET_NULL)
    product = models.ForeignKey(Product,null=True,on_delete = models.SET_NULL)
    date_create = models.DateTimeField(auto_now_add = True,null=True)
    status  = models.CharField(max_length=200,null=True,choices=STATUS)

from django.db import models
import datetime

#Category
class Category (models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

#Customers
class Customer (models.Model):
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    fullName = models.CharField(max_length=100)
    phoneNumber = models.CharField(max_length=10)
    emailID = models.EmailField(max_length=50)
    passsword = models.CharField(max_length=16)

    def __str__(self):
        return f'{self.firstName} {self.lastName}'

#Sellers
class Seller (models.Model):
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    fullName = models.CharField(max_length=100)
    phoneNumber = models.CharField(max_length=10)
    emailID = models.EmailField(max_length=50)
    passsword = models.CharField(max_length=16)
    totalProducts = models.CharField(max_length=10)
    soldProducts = models.CharField(max_length=10)
    totalRevenue = models.CharField(max_length=10)


    def __str__(self):
        return f'{self.firstName} {self.lastName}'
#Products
class Product (models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(default = 0, decimal_places=2,max_digits=5)
    Category = models.ForeignKey(Category, on_delete = models.CASCADE, default = 1)
    description = models.CharField(max_length=250, default = '', blank = True, null = True)
    image = models.ImageField(upload_to = 'uploads/product/')

    def __str__(self):
        return self.name
#Orders
class Order (models.Model):
    product = models.ForeignKey(Product, on_delete = models.CASCADE)
    customers = models.ForeignKey(Customer, on_delete = models.CASCADE)
    quantity = models.IntegerField(default=1)
    address = models.CharField(max_length=100, default = '', blank = True, null = True)
    phoneNumber = models.CharField(max_length=10)
    date = models.DateField(default = datetime.datetime.today)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.product
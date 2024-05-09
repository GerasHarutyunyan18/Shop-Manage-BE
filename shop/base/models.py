from django.db import models


# User model start
class User(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    birthDate = models.DateField(default=None, null=True)
    image = models.CharField(null=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    rate = models.IntegerField(default=0)
    token = models.CharField(max_length=255)
    createdAt = models.DateField(auto_now_add=True)
    market = models.ForeignKey('Market', on_delete=models.SET_NULL, null=True, related_name='user_market')
    company = models.ForeignKey('Company', on_delete=models.SET_NULL, null=True, related_name='user_company')
    role = models.ForeignKey('UserRole', on_delete=models.SET_NULL, null=True, related_name='user_role')
    
    def __str__(self) -> str:
        return self.email
# User model end


# Market model start
class Market(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    createdAt = models.DateField(auto_now_add=True)
    workingTimeStart = models.TimeField(default=None, null=True)
    workingTimeEnd = models.TimeField(default=None, null=True)
    image = models.CharField()
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='market_owner')

    def __str__(self) -> str:
        return self.name
# Market model end


# Company model start (its inheritancing the Market model, because of written pass)
class Company(Market):
    pass # see reason of `pass` in above comment
# Company model end


# Product model start
class Product(models.Model):
    name = models.CharField(max_length=200)
    image = models.CharField()
    market = models.ForeignKey('Market', on_delete=models.SET_NULL, null=True, related_name='product_market')
    company = models.ForeignKey('Company', on_delete=models.SET_NULL, null=True, related_name='product_company')
    price = models.IntegerField(default=0)
    currency = models.ForeignKey('Currency', on_delete=models.SET_NULL, null=True, related_name='product_currency')

    def __str__(self) -> str:
        return self.name
# Product model end


# Currency model start
class Currency(models.Model):
    name = models.CharField(max_length=100)
    token = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.name
# Currency model end

# UserRole model start
class UserRole(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name
# UserRole model end

from django.contrib import admin

from .models import User, Market, Company, Product, UserRole, Currency, CountMethod

# Register your models here.
admin.site.register(User)
admin.site.register(Market)
admin.site.register(Company)
admin.site.register(Product)
admin.site.register(UserRole)
admin.site.register(Currency)
admin.site.register(CountMethod)

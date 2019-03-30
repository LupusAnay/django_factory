from django.contrib import admin

# Register your models here.
from factory.models import Customer, Order, Detail, Component, Provider

admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(Detail)
admin.site.register(Component)
admin.site.register(Provider)

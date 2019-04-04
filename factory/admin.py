from django.contrib import admin

# Register your models here.
from rangefilter.filter import DateTimeRangeFilter

from factory.models import Customer, Order, Detail, Component, Provider


class CustomerView(admin.ModelAdmin):
    search_fields = (
        'name',
    )


class OrderView(admin.ModelAdmin):
    autocomplete_fields = ('details',)

    readonly_fields = (
        'total',
    )

    list_filter = (
        ('date', DateTimeRangeFilter),
    )
    search_fields = (
        'date',
    )


class DetailView(admin.ModelAdmin):
    autocomplete_fields = ('components',)

    search_fields = (
        'name',
    )


class ComponentView(admin.ModelAdmin):
    autocomplete_fields = ('providers',)

    search_fields = (
        'name',
    )


class ProviderView(admin.ModelAdmin):
    search_fields = (
        'name',
    )


admin.site.register(Customer, CustomerView)
admin.site.register(Order, OrderView)
admin.site.register(Detail, DetailView)
admin.site.register(Component, CustomerView)
admin.site.register(Provider, ProviderView)

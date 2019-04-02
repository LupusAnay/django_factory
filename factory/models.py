from django.db import models


# Create your models here.

class Customer(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)

    class Meta:
        permissions = (
            ("change_task_status", "Can change the status of tasks"),
            ("close_task", "Can remove a task by setting its status as closed"),
        )

    def __str__(self):
        return f'{self.name}'


class Order(models.Model):
    customer = models.ForeignKey('Customer', on_delete=models.CASCADE)
    total = models.DecimalField(decimal_places=2, max_digits=40)
    date = models.DateTimeField()
    details = models.ManyToManyField('Detail')

    def __str__(self):
        return f'Customer: {self.customer.name}; Date: {self.date}'


class Detail(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(decimal_places=2, max_digits=40)
    cost = models.DecimalField(decimal_places=2, max_digits=40)
    components = models.ManyToManyField('Component')

    def __str__(self):
        return f'Name: {self.name}; Price: {self.price}'


class Component(models.Model):
    providers = models.ManyToManyField('Provider')
    name = models.CharField(max_length=255)

    def __str__(self):
        return f'Name: {self.name}'


class Provider(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.name}'

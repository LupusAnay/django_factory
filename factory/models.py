from django.db import models


# Create your models here.

class Customer(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.name}'


class Order(models.Model):
    customer = models.ForeignKey('Customer', on_delete=models.CASCADE)
    total = models.DecimalField(decimal_places=20, max_digits=40)
    date = models.DateTimeField()
    details = models.ManyToManyField('Detail')


class Detail(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(decimal_places=20, max_digits=40)
    cost = models.DecimalField(decimal_places=20, max_digits=40)
    components = models.ManyToManyField('Component')

    def __str__(self):
        return f'{self.name}'


# class ComponentList(models.Model):
#     component = models.ForeignKey('Component', on_delete=models.CASCADE)
#     detail = models.ForeignKey('Detail', on_delete=models.CASCADE)
#     amount = models.FloatField()


class Component(models.Model):
    providers = models.ManyToManyField('Provider')
    name = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.name}'


# class Sailing(models.Model):
#     provider = models.ForeignKey('Provider', on_delete=models.CASCADE)
#     component = models.ForeignKey('Component', on_delete=models.CASCADE)
#     price = models.DecimalField(decimal_places=20, max_digits=40)


class Provider(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.name}'

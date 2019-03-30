# Create your views here.
from rest_framework.reverse import reverse
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework import permissions, authentication
from rest_framework.response import Response

from factory.models import Order, Customer, Detail, Component, Provider
from factory.serializers import OrderSerializer, CustomerSerializer, \
    DetailSerializer, ComponentSerializer, ProviderSerializer


class Customers(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = CustomerSerializer
    queryset = Customer.objects.all()


class CustomerInfo(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = CustomerSerializer
    queryset = Customer.objects.all()


class Details(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = DetailSerializer
    queryset = Detail.objects.all()


class DetailsInfo(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = DetailSerializer
    queryset = Detail.objects.all()


class Orders(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = OrderSerializer
    queryset = Order.objects.all()


class OrderInfo(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = OrderSerializer
    queryset = Order.objects.all()


class Components(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = ComponentSerializer
    queryset = Component.objects.all()


class ComponentInfo(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = ComponentSerializer
    queryset = Component.objects.all()


class Providers(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = ProviderSerializer
    queryset = Provider.objects.all()


class ProviderInfo(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = ProviderSerializer
    queryset = Provider.objects.all()


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'Orders': reverse('order-list', request=request, format=format),
        'Customers': reverse('customer-list', request=request, format=format),
        'Details': reverse('detail-list', request=request, format=format),
        'Components': reverse('component-list', request=request, format=format),
        'Providers': reverse('provider-list', request=request, format=format),
    })

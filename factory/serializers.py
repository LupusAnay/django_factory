from rest_framework import serializers

from factory.models import Order, Customer, Detail, Provider, Component


class CustomerSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='customer-detail',
                                               read_only=True)

    class Meta:
        model = Customer
        fields = ('id', 'name', 'address', 'url')


class OrderSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='order-detail',
                                               read_only=True)

    class Meta:
        model = Order
        fields = ('id', 'customer', 'total', 'date', 'details', 'url')


class ComponentSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='component-detail',
                                               read_only=True)

    class Meta:
        model = Component
        fields = ('id', 'name', 'providers', 'url')


class DetailSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='detail-detail',
                                               read_only=True)

    class Meta:
        model = Detail
        fields = ('id', 'name', 'price', 'cost', 'url', 'components')


class ProviderSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='provider-detail',
                                               read_only=True)

    class Meta:
        model = Provider
        fields = ('id', 'name', 'address', 'url')

from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from factory import views

urlpatterns = [
    path('', views.api_root),
    path('customers/', views.Customers.as_view(),
         name='customer-list'),
    path('customers/<int:pk>', views.CustomerInfo.as_view(),
         name='customer-detail'),
    path('orders/', views.Orders.as_view(),
         name='order-list'),
    path('orders/<int:pk>', views.OrderInfo.as_view(),
         name='order-detail'),
    path('details/', views.Details.as_view(),
         name='detail-list'),
    path('details/<int:pk>', views.DetailsInfo.as_view(),
         name='detail-detail'),
    path('components/', views.Components.as_view(),
         name='component-list'),
    path('components/<int:pk>', views.ComponentInfo.as_view(),
         name='component-detail'),
    path('providers/', views.Providers.as_view(),
         name='provider-list'),
    path('providers/<int:pk>', views.ProviderInfo.as_view(),
         name='provider-detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)

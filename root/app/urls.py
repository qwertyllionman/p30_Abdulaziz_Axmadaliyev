from django.urls import path

from .views import homeView, shopView, cartView

urlpatterns = [
    path('home', homeView, name='home'),
    path('shop', shopView, name='shop'),
    path('cart', cartView, name='cart')
]

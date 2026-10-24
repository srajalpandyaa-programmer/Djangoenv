from django.urls import path
from . import views
urlpatterns = [
    
    #path('shop/', views.home, name='home'),
    #path('shop/products/', views.products, name='products')
    
    path('', views.product_list,name = 'product_list')
]
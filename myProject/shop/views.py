from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
'''
def home(request):
    return HttpResponse('<h1>Welcome to my Shop</h1>')

def products(request):
    return HttpResponse("Product's about page")
'''

def product_list(request):
    return render(request, 'shop/product_list.html')
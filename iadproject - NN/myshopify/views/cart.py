from django.views import View
from django.shortcuts import render,redirect
from django.http import HttpResponse
from myshopify.models.product import Product
from myshopify.models.category import Category
from myshopify.models.customer import Customer
from django.contrib.auth.hashers import make_password,check_password
from django.views import View


class Cart(View):
    def get (self,request):
        ids=(list(request.session.get('cart').keys()))
        productslist= Product.get_products_by_id(ids)
        print(productslist)
        return render(request,'order/carttry.html',{'products':productslist})

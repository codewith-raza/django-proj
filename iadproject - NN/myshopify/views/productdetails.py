from django.views import View
from django.shortcuts import render,redirect
from django.http import HttpResponse
from myshopify.models.product import Product
from myshopify.models.category import Category
from myshopify.models.customer import Customer
from django.contrib.auth.hashers import make_password,check_password
from django.views import View
from myshopify.models.orders import Order
from myshopify.models.productreview import Productreview
from django.contrib import messages
class ProductDetails(View):
    def get(self,request,myid):
        print("PRODUCT DETAILS",myid)
        product=Product.objects.get(id=myid)
        print(product.name,"product")
        reviews=Productreview.objects.filter(product=product)
        return render(request,'order/productdetailtry.html',{'product':product,'reviews':reviews})#newly added

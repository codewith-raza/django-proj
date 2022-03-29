from django.views import View
from django.shortcuts import render,redirect
from django.http import HttpResponse
from myshopify.models.product import Product
from myshopify.models.category import Category
from myshopify.models.customer import Customer
from django.contrib.auth.hashers import make_password,check_password
from django.views import View
from myshopify.models.orders import Order

class Orders(View):
    def post(self,request):
        address=(request.POST.get('address'))
        phone=(request.POST.get('phone'))
        customer=request.session.get('customer_id')
        cart=request.session.get('cart')
        products=Product.get_products_by_id(list(cart.keys()))
        print(address," ", phone,customer,cart,products,"ALL THINGS")
        for product in products:
            order=Order(customer=Customer(id=customer),
                          product=product,
                          price=product.price,
                          quantity=cart.get(str(product.id)),address=address,
                          phone=phone)
            print(order)
            order.save()

            #print(order.place_order(),"ORDER PLACED")
        request.session['cart']={}

        return redirect ('cart')

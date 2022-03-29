from django.views import View
from django.shortcuts import render,redirect
from django.http import HttpResponse

from myshopify.models.customer import Customer
from django.contrib.auth.hashers import make_password,check_password
from django.views import View
from myshopify.models.orders import Order

from myshopify.middlewares.auth import auth_middleware



class OrderFinal(View):

    def get(self,request):
        customer=request.session.get('customer_id')
        #name=request.session.get('customer_first_name')
        orders=Order.get_orders_by_customer(customer)
        print(orders,"order------",customer)
        return render(request,'order/order.html',{'orders':orders})

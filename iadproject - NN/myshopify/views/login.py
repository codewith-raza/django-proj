from django.views import View
from django.shortcuts import render,redirect
from django.http import HttpResponse
from myshopify.models.product import Product
from myshopify.models.category import Category
from myshopify.models.customer import Customer
from django.contrib.auth.hashers import make_password,check_password
from django.views import View

class Login(View):
    return_url=None
    def get(self,request):
        Login.return_url=request.GET.get('return_url')

        #self added
        # first_name = request.session.get('first_name')
        # if not first_name:
        #     pass
        #self added


        return render(request,'order/login.html')
    def post(self,request):
        email=request.POST.get('email')
        password=request.POST.get('password')
        customer=Customer.get_customer_by_email(email)
        error_message=None
        if customer:
            flag=check_password(password,customer.password)
            if flag:
                request.session['customer']=customer.id

                request.session['customer_id']=customer.id
                #request.session['email']=customer.email
                request.session['customer_first_name']=customer.first_name
                return redirect('productspage')

            else:
                error_message='Email or Password Invalid'


        else:
            error_message='Email or Password Invalid'
        print(customer,"QUERY")
        print(email,password,"EMAILPASS")
        return render(request,'order/login.html',{'error':error_message})




def logout(request):
    request.session.clear()
    return redirect('login')

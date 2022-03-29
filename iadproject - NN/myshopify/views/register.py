from django.views import View
from django.shortcuts import render,redirect
from django.http import HttpResponse
from myshopify.models.product import Product
from myshopify.models.category import Category
from myshopify.models.customer import Customer
from django.contrib.auth.hashers import make_password,check_password
from django.views import View


class Register(View):
    def ValidateCustomer(self,customer):
        ##VALIDATE
        error_message=None
        if (not customer.first_name):
            error_message="FIRST NAME Required !!"
        if customer.first_name:
            if len(customer.first_name)<4:
                error_message="First name must be more than 4"
        if len(customer.last_name)==0:
            error_message="last name Required !!"
            #print(error_message,"ERROR LASRuuuu ***********************************")
        if customer.last_name:
          if len(customer.last_name)<4:
            error_message='Last Name length issue'
            #print(error_message,"ERROR LASR ***********************************")
        if not customer.phone_name:
            error_message='Phone required'
        if len(customer.phone_name)<11:
            error_message='Phone number can"t be less than 10'
        if not customer.email:
            error_message='Email Required'
        if len(customer.email) <5:
            error_message='length of email should be greater than 5'
        if customer.isExists():
            error_message="email already exist !!"
        print(error_message,"ERROR***********************************")
        return error_message
    def get(self,request):
        return render(request,'order/register.html')
    def post(self,request):
        print("WE ARE IN REGISTER USER FUNCTION")
        postData=request.POST
        first_name=postData.get('firstname')
        last_name=postData.get('lastname')
        email=postData.get('email')
        phone=postData.get('phone')
        password=postData.get('password')

        value = {
            'first_name': first_name,
            'last_name': last_name,
            'phone': phone,
            'email': email
        }
        customer=Customer(first_name=first_name,
                         last_name=last_name,
                         phone_name=phone,email=email,password=password)
        error_message=self.ValidateCustomer(customer)


        if not error_message:
                print(first_name,last_name)
                customer.password=make_password(customer.password)

                customer.register()
                return redirect('productspage')
        else:
             data={
              'error':error_message,
              'values':value
             }
             return render(request,'order/register.html',data)

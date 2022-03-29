from django.views import View
from django.shortcuts import render,redirect
from django.http import HttpResponse
from myshopify.models.product import Product
from myshopify.models.category import Category
from myshopify.models.customer import Customer
from django.contrib.auth.hashers import make_password,check_password
from django.views import View

class Index(View):
    def get(self,request):
        cart = request.session.get('cart')
        if not cart:
            request.session['cart'] = {}
        prod=None

        print(prod)
        categories=Category.get_all_categories();
        categoryID=request.GET.get('category')
        if categoryID:
            prod=Product.get_all_products_by_category_id(categoryID)
        else:
            prod=Product.get_all_products();
        data={}
        data['products']=prod
        data['categories']=categories
        print("YOU Are",request.session.get('customer_first_name'))

        return render(request,'order/indextry.html',data)
    def post(self,request):
        product=request.POST.get('product')
        remove=request.POST.get('remove')
        cart=request.session.get('cart')

        if cart:
            quantity=cart.get(product)
            if quantity:
                if remove:
                    if quantity<=1:
                        cart.pop(product)
                    else:
                       cart[product]=quantity-1
                else:
                     cart[product]=quantity+1
            else:
                cart[product]=1
        else:
            cart={}
            cart[product]=1
        request.session['cart']=cart
        print(request.session['cart'],"CART")

        #print(product,"----Product Id----")
        return redirect('productspage')

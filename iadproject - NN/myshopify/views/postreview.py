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
def postreview(request):
    if request.method=="POST":
        productid=request.POST.get("productid")
        review=request.POST.get("review")
        product=Product.objects.get(id=productid)
        customer=request.session.get('customer_id')
        comment=Productreview(review=review,customer=Customer(id=customer),product=product)
        comment.save()
        messages.success(request,"Your Comment has been posted successfuly")
    return redirect(f'productdetails/{productid}')
def search(request):

    if request.method=="POST":
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
        searched= request.POST.get('searched')
        print(searched,"searched")

        producting=Product.objects.filter(name__icontains=searched)
        data['products']=producting
    return render (request,'order/searchtry.html',data)

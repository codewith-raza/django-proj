from django.urls import path
from .views.home import Index
from .views.register import Register
from .views.login import Login,logout
from .views.cart import Cart
from .views.order import Orders
from .views.order_final import OrderFinal
from .middlewares.auth import auth_middleware
from .views.productdetails import ProductDetails
from .views.contact import Contact
from .views.postreview import postreview,search
from .views.check import Check
urlpatterns = [
    path('postreview',postreview,name="postreview"),
    path('',Index.as_view(),name="productspage"),
    path('register',Register.as_view(),name='register'),
    path('login',Login.as_view(),name='login'),
    path('logout',logout,name='logout'),
    path('cart',Cart.as_view(),name='cart'),
    path('check-out',Orders.as_view(),name="check-out"),#checkout
    path('orders', auth_middleware( OrderFinal.as_view()),name='orders'),

    path('productdetails/<int:myid>',ProductDetails.as_view(),name="productdetails"),
    path('contact',Contact.as_view(),name="contact"),
    path('search',search,name="search"),
    path('check',Check.as_view(),name="check")
]

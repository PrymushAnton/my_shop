"""
URL configuration for Order project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
import Main_page.views as main_page_views
import Product_page.views as product_page_views
import Shopping_cart_page.views as shopping_cart_views
import Contact_page.views as contact_views
import Authorization_Registration.views as authorization_registration_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main_page_views.main_page, name= "main_page"),
    path('product_page/', product_page_views.product_page, name= "product_page"),
    path('cart_page/', shopping_cart_views.cart_page, name= "cart_page"),
    path('contact_page/', contact_views.contact_page, name= "contact_page"),
    path('authorization_page/', authorization_registration_views.authorization, name= "authorization_page"),
    path('registration_page/', authorization_registration_views.registration, name= "registration_page"),
    path('product_page2/', product_page_views.product_page2, name= "product_page2"),
    path('product_page3/', product_page_views.product_page3, name= "product_page3"),
    path('product_page4/', product_page_views.product_page4, name= "product_page4"),
    path('product_page5/', product_page_views.product_page5, name= "product_page5"),
    
]

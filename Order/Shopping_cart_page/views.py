from django.shortcuts import render
from .models import Cart

# Create your views here.
def cart_page(request):
    cart = Cart.objects.all()
    return render(request, 'Shopping_cart_page/cart.html', context={"cart": cart})
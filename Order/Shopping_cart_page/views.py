from django.shortcuts import render

# Create your views here.
def cart_page(request):
    return render(request, 'Shopping_cart_page/cart.html')
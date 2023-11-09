from django.shortcuts import render
from .models import Cart
from Main_page.models import Main

# Create your views here.
def cart_page(request):
    cart = Cart.objects.get(user_id=request.user.id)
    context = {}
    context["products_cart"] = []
    try:
        list_id = cart.product_id.split(",")
        for i in list_id:
            context["products_cart"].append(Main.objects.filter(id = i))
    except:
        pass
    return render(request, 'Shopping_cart_page/cart.html', context)

def delete_product_cart(request):
    context={}
    return render(request, 'Shopping_cart_page/cart.html', context)


def add_cart_product(request):
    if request.method == 'POST':
        ids = request.POST.get("ids")
        print(request.user.id)
        if ids:
            cart = Cart.objects.get(user_id=request.user.id)
            cart.product_id += f"{ids},"
            cart.save()
    return render(request, 'Shopping_cart_page/cart.html')
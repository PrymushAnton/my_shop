from django.shortcuts import render

# Create your views here.
def product_page(request):
    return render(request, 'Product_page/product_page1.html', )

def product_page2(request):
    return render(request, 'Product_page/product_page2.html', )

def product_page3(request):
    return render(request, 'Product_page/product_page3.html', )

def product_page4(request):
    return render(request, 'Product_page/product_page4.html', )

def product_page5(request):
    return render(request, 'Product_page/product_page5.html', )
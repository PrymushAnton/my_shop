from django.shortcuts import render
from Main_page.models import Main

# Create your views here.
def product_page(request):
    context = {}
    context['product'] = Main.objects.get(id = request.POST.get('ids'))
    print(context['product'])
    return render(request, 'Product_page/product_page1.html', context)
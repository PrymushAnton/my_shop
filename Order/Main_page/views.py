from django.shortcuts import render
from .models import Main

# Create your views here.
def main_page(request):
    
    product = Main.objects.all()
    auth = False
    
    return render(request, 'Main_page/main.html', context = {'products': product, "auth": auth})
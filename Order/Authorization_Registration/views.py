from django.shortcuts import render

# Create your views here.
def authorization(request):
    return render(request, 'Authorization_Registration/authorization.html')

def registration(request):
    return render(request, 'Authorization_Registration/registration.html')

def register(request):
    if request.method == 'POST':
        print(request)
    return render(request, 'Authorization_Registration/registration.html')

def login(request):
    if request.method == 'POST':
        print(request.POST)
    return render(request, 'Authorization_Registration/authorization.html')
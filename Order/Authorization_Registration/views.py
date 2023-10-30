from django.shortcuts import render

# Create your views here.
def authorization(request):
    return render(request, 'Authorization_Registration/authorization.html')

def registration(request):
    return render(request, 'Authorization_Registration/registration.html')

def register_request(request):
    if request.method == 'POST':
        print(1)
    return render(request, 'Authorization_Registration/registration.html')
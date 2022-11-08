from django.shortcuts import render

# Create your views here.
def Town1(request):
    return render(request, 'Town1/index.html')

def Town2(request):
    return render(request, 'Town2/index.html')

def Town3(request):
    return render(request, 'Town3/index.html')

def index(request):
    return render(request, 'Town/index.html')
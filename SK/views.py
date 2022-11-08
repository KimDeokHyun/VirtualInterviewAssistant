from django.shortcuts import render

# Create your views here.
def SK1(request):
    return render(request, 'SK1/index.html')

def SK2(request):
    return render(request, 'SK2/index.html')

def SK3(request):
    return render(request, 'SK3/index.html')

def index(request):
    return render(request, 'SK/index.html')
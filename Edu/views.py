from django.shortcuts import render

# Create your views here.
def Edu1(request):
    return render(request, 'Edu1/index.html')

def Edu2(request):
    return render(request, 'Edu2/index.html')

def Edu3(request):
    return render(request, 'Edu3/index.html')

def index(request):
    return render(request, 'Edu/index.html')
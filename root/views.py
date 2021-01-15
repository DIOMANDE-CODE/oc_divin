from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,'index.html')

def merci(request):
    return render(request,'remerciement.html')
from django.shortcuts import render

# Create your views here.

def index(request):

    return render(request, 'produto/index.html')

def produtos(request):

    return render(request, 'produto/produtos.html')

def car(request):

    return render(request, 'produto/car.html')

def contato(request):

    return render(request, 'produto/contato.html')
from django.shortcuts import render, HttpResponse, redirect

def index(request):
    return render(request, 'index.html')
def antecedentes(request):
    return render(request, 'antecedentes.html')
def ayuntamiento(request):
    return render(request, 'ayuntamiento.html')
def contacto(request):
    return render(request, 'contacto.html')
def sevac(request):
    return render(request, 'sevac.html')
def transparencia(request):
    return render(request, 'transparencia.html')
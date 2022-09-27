from django.shortcuts import render

def index(request):
    return render(request, 'contatos/index.html')

def detalhes(request):
    return render(request, 'contatos/detalhes.html')

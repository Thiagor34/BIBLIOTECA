from django.shortcuts import render, HttpResponse
from . models import Midias

# Create your views here.
def index(request):
    midias = Midias.objects.all()    
    return render(request, 'pages/index.html', {'midias':midias})


def search(request): 
    q = request.GET.get('search')   
    midias = Midias.objects.filter(title__icontains=q)    
    return render(request, 'pages/index.html', {'midias':midias})
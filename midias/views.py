from django.shortcuts import render, redirect, get_object_or_404
from . models import Midias
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(redirect_field_name='login')
def index(request):
    midias = Midias.objects.all()    
    return render(request, 'pages/index.html', {'midias':midias})


def search(request): 
    q = request.GET.get('search')   
    midias = Midias.objects.filter(title__icontains=q)    
    return render(request, 'pages/index.html', {'midias':midias})

def detalhes(request, id):
    midia = get_object_or_404(Midias, id=id)
    return render(request, 'pages/detalhes.html', {'midia':midia})

def deletar(request, id):
    midias = Midias.objects.get(id=id)
    midias.delete()
    return redirect('home')  

def adicionar(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        release_year = request.POST.get('release_year')
        director = request.POST.get('director')
        description = request.POST.get('description')
        created_at = request.POST.get('created_at')
        
        nova_midia = Midias(usuario_id=request.user.id,title=title, release_year=release_year, director=director, description=description, created_at=created_at)
        nova_midia.save()
        return redirect('home')
    
    else:
        return render(request, 'pages/adicionar.html')
    
    
def editar(request, id):
    midia = Midias.objects.get(id=id)    
    if request.method == 'POST':
        title = request.POST.get('title')
        release_year = request.POST.get('release_year')
        director = request.POST.get('director')
        description = request.POST.get('description')
        created_at = request.POST.get('created_at')

        
        midia.title = title
        midia.release_year = release_year
        midia.director = director
        midia.description = description
        midia.created_at = created_at

        midia.save()  
              
        return redirect('home')
       
    else:
            
        return render(request, 'pages/editar.html', {'midia':midia})

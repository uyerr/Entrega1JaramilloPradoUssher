from django.shortcuts import render


def index(request):
    
    return render(request, 'Pagina_Blog/index.html')

def about(request):
    
    return render(request, 'Pagina_Blog/about.html')



    
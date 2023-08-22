from django.shortcuts import render

# Create your views here.
def index(request):
    """Главная страница"""
    return render(request, 'publications/index.html')
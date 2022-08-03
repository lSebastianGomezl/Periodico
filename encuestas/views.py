from cgitb import text
from django.shortcuts import render
from .models import Notice

# Create your views here.

def index(request):
    notice = Notice.objects.all()
    data = {
        'noticias': notice
    }
    return render(request, 'index.html', data)


def deportes(request):

    return render(request, 'deportes.html')


def contacto(request):

    return render(request, 'contacto.html')
from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse
from django.views.generic import ListView, DetailView

from .models import Periodo
from .forms import PeriodoForm

def index(request):
    return HttpResponse("hola este es el index")

def periodo(request):
    lista = Periodo.objects.order_by('id')
    context = {
        'lista': lista,
    }
    return render(request, 'periodo/index.html' ,context)

def periodo_view(request, periodo_id):
    periodo = get_object_or_404(Periodo, pk=periodo_id)
    return render(request, 'periodo/periodo_view.html', {'periodo': periodo})

def periodo_create(request):
    if request.method == 'POST':
        form = PeriodoForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('periodo')
    else:
        form = PeriodoForm
    return render(request, 'periodo/periodo_form.html', {'form':form})
        

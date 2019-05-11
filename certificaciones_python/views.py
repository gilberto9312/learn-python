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

def periodo_edit(request, periodo_id):
    periodo = Periodo.objects.get(id=periodo_id)
    if request.method == 'GET':
        form = PeriodoForm(instance = periodo)
    else:
        form = PeriodoForm(request.POST, instance = periodo)
        if form.is_valid():
            form.save()
        return redirect('periodo')
    return render(request, 'periodo/periodo_form.html', {'form':form})

def periodo_delete(request, periodo_id):
    periodo = Periodo.objects.get(id=periodo_id)
    if request.method == 'POST':
        periodo.delete()
        return redirect('periodo')
    return render(request, 'periodo/periodo_delete.html',{'periodo' : periodo}) 
        

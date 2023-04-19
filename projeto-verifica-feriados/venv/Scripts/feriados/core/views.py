from django.shortcuts import render
from django.http import HttpResponse
from datetime import date
from core.models import FeriadoModel


def feriado(request):
    qs = FeriadoModel.objects.all()
    data_atual = date.today()
    nome = 'Hoje não é feriado'
    for feriado in qs:
        if(feriado.dia == data_atual.day and feriado.mes == data_atual.month):
            nome = feriado.nome
    contexto = {
        'feriado' : nome
    } 
    return render(request, 'feriado.html', contexto)

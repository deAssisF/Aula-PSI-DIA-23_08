from django.shortcuts import render
from .models import tarefa
from datetime import date
# Create your views here.

def index(request):
    hoje = date.today()
    tarefas = tarefa.objects.all()

    context = {
        "tarefas": tarefas,
        "hoje": hoje,
    }

    return render(request, 'index.html', context)
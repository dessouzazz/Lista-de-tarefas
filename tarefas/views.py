from django.shortcuts import render

def lista_tarefas(request):
    tarefas = ["Estudar Django", "Criar um projeto", "Revisar o conteúdo"]
    return render(request, 'lista_tarefas.html', {'tarefas':
tarefas})
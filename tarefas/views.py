from django.shortcuts import render, redirect,  get_object_or_404
from .models import Tarefa
from django.contrib import messages 
from django.core.exceptions import ValidationError
from django.contrib.auth.decorators import login_required

@login_required
def lista_tarefas(request):
    if request.method == 'POST':
        titulo = request.POST.get('titulo')
        if titulo:
            tarefa = Tarefa(titulo=titulo, usuario=request.user)
            try:
                tarefa.full_clean()
                tarefa.save()
                messages.success(request, 'Tarefa adicionada com sucesso!')
            except ValidationError as e:
                messages.error(request, e.message_dict['titulo'][0])
        else:
            messages.error(request, 'O título da tarefa não pode ser vazio.')

        return redirect('lista_tarefas')

    tarefas = Tarefa.objects.filter(usuario=request.user)
    return render(request, 'lista_tarefas.html', {'tarefas': tarefas})

def concluir_tarefa(request, id):
    tarefa = get_object_or_404(Tarefa, id=id)
    tarefa.concluida = True
    tarefa.save()
    return redirect('lista_tarefas')

def excluir_tarefa(request, id):
    tarefa = get_object_or_404(Tarefa, id=id)
    tarefa.delete()
    return redirect('lista_tarefas')

def editar_tarefa(request, id):
    tarefa = get_object_or_404(Tarefa, id=id)

    if request.method == 'POST':
        novo_titulo = request.POST.get('titulo')
        if novo_titulo:
            tarefa.titulo = novo_titulo
            tarefa.save()
            return redirect('lista_tarefas')
    return render(request, 'editar_tarefa.html', {'tarefa': tarefa})
    

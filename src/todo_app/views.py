from django.shortcuts import render
from django.http import HttpResponseRedirect

from .models import TodoItem

def todo_view(request):
    all_todo_items = TodoItem.objects.all()
    context = {
        'all_todo_items': all_todo_items,
    }
    return render(request, 'todo_app/todo.html', context)


def add_todo(request):
    """add_todo() creates new todo item into database and redirect to the list of todo item page"""
    todo_item = TodoItem(content=request.POST['content'])
    todo_item.save()
    return HttpResponseRedirect('/todo/')


def delete_todo(request, todo_id):
    """delete_todo() deletes the todo item using it's id"""
    todo_item = TodoItem.objects.get(id=todo_id)
    todo_item.delete()
    return HttpResponseRedirect('/todo/')

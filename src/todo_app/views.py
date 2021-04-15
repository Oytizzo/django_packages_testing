from django.shortcuts import render
from django.http import HttpResponse


def todo_view(request):
    return render(request, 'todo_app/todo.html')

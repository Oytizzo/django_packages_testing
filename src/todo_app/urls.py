from django.urls import path

from .views import todo_view, add_todo, delete_todo

urlpatterns = [
    path('', todo_view, name='todo-view'),
    path('add-todo/', add_todo, name='add-todo'),
    path('delete-todo/<int:todo_id>/', delete_todo, name='delete-todo')
]
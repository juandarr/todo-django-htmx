from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Todo

# Rendering home page
def index(request):
    todos = Todo.objects.all().order_by('-id')
    context = {'todos': todos,}
    template = loader.get_template('index.html')
    return HttpResponse(template.render(context, request))

# Creating a new Todo
def create_todo(request):
    description = request.POST.get('description')
    todo = Todo.objects.create(description=description)
    todo.save()
    todos = Todo.objects.all().order_by('-id')
    context = { 'todos': todos}
    template = loader.get_template('todos.html')
    return HttpResponse(template.render(context, request)) 

# Toggle completed
def mark_todo(request, pk):
    todo = Todo.objects.get(pk=pk)
    todo.complete = not(todo.complete)
    todo.save()
    todos = Todo.objects.all().order_by('-id')
    context = { 'todos': todos}
    template = loader.get_template('todos.html')
    return HttpResponse(template.render(context, request)) 

# Delete todo
def delete_todo(request, pk):
    todo = Todo.objects.get(pk=pk)
    todo.delete()
    todos = Todo.objects.all().order_by('-id')
    context = { 'todos': todos}
    template = loader.get_template('todos.html')
    return HttpResponse(template.render(context, request)) 

# Edit todo description
def edit_todo(request, pk):
    todo = Todo.objects.get(pk=pk)
    if request.method == 'POST':
        todo.description = request.POST.get('description')
        todo.save()
        todos = Todo.objects.all().order_by('-id')
        context = { 'todos': todos}
        template = loader.get_template('todos.html')
        return HttpResponse(template.render(context, request)) 
    context = {'todo': todo}
    template = loader.get_template('edit.html')
    return HttpResponse(template.render(context, request)) 
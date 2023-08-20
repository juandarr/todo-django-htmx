from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Todo

def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())

def todos(request):
    todos = Todo.objects.all().values()
    template = loader.get_template('todos.html')
    context = {'todos': todos,}
    return HttpResponse(template.render(context,request))
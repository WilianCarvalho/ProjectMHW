from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse

def helloWord(request):
    return HttpResponse('Hello Word')

def taskslist(request):
    return render(request, 'tasks/list.html')
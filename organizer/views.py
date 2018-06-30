from django.shortcuts import render
from django.http import HttpResponse
from .models import TodoItem

def index(request):
    task_list = TodoItem.objects.all()[:5]
    output = ", ".join([i.description for i in task_list])
    return HttpResponse(output)

def detail(request, item_id):
    return HttpResponse("todo item details: %s" % item_id)

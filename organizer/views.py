from django.shortcuts import render
from django.http import HttpResponse
from .models import TodoItem
# from django.template import loader

def index(request):
    task_list = TodoItem.objects.all()[:5]
    # template = loader.get_template('organizer/index.html')
    context = {
        'task_list': task_list,
    }
    # return HttpResponse(template.render(context, request))
    return render(request, 'organizer/index.html', context)

def detail(request, item_id):
    # return HttpResponse("todo item details: %s" % item_id)
    task = TodoItem.objects.get(pk=item_id)
    return render(request, 'organizer/detail.html', {'task': task})

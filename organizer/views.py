from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import Task
# from django.template import loader

def index(request):
    task_list = Task.objects.all()[:5]
    # template = loader.get_template('organizer/index.html')
    context = {
        'task_list': task_list,
    }
    # return HttpResponse(template.render(context, request))
    return render(request, 'organizer/index.html', context)

def detail(request, item_id):
    # return HttpResponse("todo item details: %s" % item_id)
    try:
        task = Task.objects.get(pk=item_id)
    except Task.DoesNotExist:
        raise Http404("Task does not exist")
    return render(request, 'organizer/detail.html', {'task': task})

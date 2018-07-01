
from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404
from django.views import generic
# from django.template import loader
from .models import Task

class IndexView(generic.ListView):
    template_name = 'organizer/index.html'

    def get_queryset(self):
        return Task.objects.all()[:5]

class DetailView(generic.DetailView):
    model = Task
    template_name = 'organizer/detail.html'


# def index(request):
#     task_list = Task.objects.all()[:5]
#     # template = loader.get_template('organizer/index.html')
#     context = {
#         'task_list': task_list,
#     }
#     # return HttpResponse(template.render(context, request))
#     return render(request, 'organizer/index.html', context)
#
# def detail(request, item_id):
#     # return HttpResponse("todo item details: %s" % item_id)
#
#     # very common pattern => there is a shortcut for it
#     # try:
#     #     task = Task.objects.get(pk=item_id)
#     # except Task.DoesNotExist:
#     #     raise Http404("Task does not exist")
#     task = get_object_or_404(Task, pk=item_id)
#     return render(request, 'organizer/detail.html', {'task': task})


from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views import generic
# from django.template import loader
from .models import Task

class IndexView(generic.ListView):
    def get_queryset(self):
        return Task.objects.filter(complete=False)[:15]

class DetailView(generic.DetailView):
    model = Task

class CreateView(generic.CreateView):
    model = Task
    fields = ['description', 'time_estimate', 'due_date']

class UpdateView(generic.UpdateView):
    model = Task
    fields = ['description', 'time_estimate', 'due_date', 'complete']

class DeleteView(generic.DeleteView):
    model = Task
    success_url = reverse_lazy('organizer:index')

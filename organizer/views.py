
from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404
from django.views import generic
# from django.template import loader
from .models import Task

class IndexView(generic.ListView):
    def get_queryset(self):
        return Task.objects.all()[:5]

class DetailView(generic.DetailView):
    model = Task

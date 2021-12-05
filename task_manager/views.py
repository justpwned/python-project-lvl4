from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import DetailView

def index(request):
    return render(request, 'task_manager/index.html')


def create_user(request):
    return render(request, 'task_manager/create_user.html')
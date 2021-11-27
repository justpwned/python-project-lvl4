from django.http import HttpResponse
from django.shortcuts import render
from django.contrib import messages


def index(request):
    return render(request, 'task_manager/index.html')


from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse('Страница на которой будет изображен контент про самолеты!!!')

def categories(request):
    return HttpResponse('Статьи по категориям')

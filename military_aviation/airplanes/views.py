from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render

from .models import Airplanes

menu = ['О сайте', 'Добавить статью', 'Обратная связь', 'Войти']


def index(request):
    posts = Airplanes.objects.all()
    return render(request, 'airplanes/index.html', {'title': 'Главная страница', 'menu': menu, 'posts': posts})


def about(request):
    return render(request, 'airplanes/about.html', {'title': 'О сайте', 'menu': menu})


def categories(request):
    return HttpResponse('Статьи по категориям')


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>СТРАНИЦА НЕ НАЙДЕНА!</h1><h2>ошибка 404</h2>')

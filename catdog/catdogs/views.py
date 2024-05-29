from django.http import HttpResponse
from django.shortcuts import render


def index(request): # request это ссылка на спецкласс HttpRequest - (содержит информация о запросе)
    return HttpResponse('Страница приложения catdogs')

def breed_of_cats(request):    # фунция представление
    return HttpResponse('Тут будет список пород кошек')

def breed_of_dogs(request):    # фунция представление
    return HttpResponse('Тут будет список пород собак')

def exapmle_for_tag(request):    # фунция представление
    return HttpResponse('<h1>Просто посмотреть как ведет себя тег h1</h1>')
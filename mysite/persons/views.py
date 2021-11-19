from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def index(request):
    return HttpResponse("Страница приложения Person")


def categories(request):
    return HttpResponse("<h1>Статья по категориям</h1>")
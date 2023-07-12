from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse('<a href="http://127.0.0.1:8000/lesson_4"> Тык </a>')

def lesson_4(request):
    return HttpResponse('Домашка по 4 занятию')

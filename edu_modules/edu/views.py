from django.shortcuts import render
from django.http import HttpResponse


def home(request):
	return HttpResponse('<h1>Главная</h1>')
 
def education(request):
	return HttpResponse('<h1>Образовательные модули</h1>')
from django.shortcuts import render
from django.http import HttpResponse, HttpRequest

from .models import EducationalModules


def home(request: HttpRequest) -> HttpResponse:
	"""Модуль отвечающий за главную страницу"""
	return render(request, 'home.html')
 
def education(request: HttpRequest) -> HttpResponse:
	"""Модуль отвечающий за страницу сообщества"""
	edu_list = EducationalModules.objects.all()
	context = {
		'edu_list': edu_list,
	}
	return render(request, 'education.html', context)

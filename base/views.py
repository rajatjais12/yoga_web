from django.shortcuts import render
from django.http import HttpResponse

def Home_Page(request):
	return HttpResponse('hello, word')

# Create your views here.

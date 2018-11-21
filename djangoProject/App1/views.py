from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse


def index(request):
    return HttpResponse("test view index")

def detail(request,num):
    return HttpResponse('detail:{0}'.format(num))
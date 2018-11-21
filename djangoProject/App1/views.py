from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from .models import Grades,Students


def index(request):
    return HttpResponse("test view index")


def detail(request, num):
    return HttpResponse('detail:{0}'.format(num))


def grades(request):
    gradelist = Grades.objects.all()
    return render(request, 'App1/grades.html', {"grades": gradelist})


def students(request):
    studentslist = Students.objects.all()
    return render(request, 'App1/students.html', {"students": studentslist})

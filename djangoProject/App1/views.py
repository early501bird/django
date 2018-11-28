from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from .models import Grades, Students


def index(request):
    return HttpResponse("test view index")


def detail(request, num):
    return HttpResponse('detail:{0}'.format(num))


def grades(request):
    gradelist = Grades.objects.all()
    return render(request, 'App1/grades.html', {"grades": gradelist})


def students(request):
    studentslist = Students.stuObj2.all()
    return render(request, 'App1/students.html', {"students": studentslist})


def gradesStudents(request, id):
    grades = Grades.objects.get(pk=id)
    stus = grades.students_set.all()
    return render(request, 'App1/students.html', {'students': stus})


def addStudent(request):
    grade = Grades.objects.get(pk=1)
    stu = Students.createStudents('刘德华', 35, True, 'my name is liu de hua', grade, '2018-08-22', '2018-08-22')
    stu.save()
    return HttpResponse("success add student:" + stu.name)


def addStudent2(request):
    grade = Grades.objects.get(pk=1)
    stu = Students.stuObj2.createStudents('张学友', 55, False, 'my name is zhangxy', grade, '2018-08-22', '2018-08-22')
    stu.save()
    return HttpResponse("success add student:" + stu.name)


# 学生分页
def studentByPage(request, page):
    page = int(page)
    studentslist = Students.stuObj2.all()[(page - 1) * 2:page * 2]
    return render(request, 'App1/students.html', {"students": studentslist})


def studentSearch(request, info):
    # studentslist = Students.stuObj2.filter(name__contains=info)
    # studentslist = Students.stuObj2.filter(name__startswith=info)
    # studentslist = Students.stuObj2.filter(pk__in=[2,4,6])
    # studentslist = Students.stuObj2.filter(age__gt=18)
    studentslist = Students.stuObj2.filter(lastTime__year=int(info))
    # studentslist = Students.stuObj2.filter(Students__content__contains=info)

    return render(request, 'App1/students.html', {"students": studentslist})


from django.db.models import F, Q


def gradesCmp(reaquest):
    g = Grades.objects.filter(girlnum__gt=F('boynum'))
    return HttpResponse(g)


def gradesOR(reaquest):
    g = Grades.objects.filter(~Q(pk__lte=1))
    return HttpResponse(g)
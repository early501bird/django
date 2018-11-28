# !c:\Program Files (x86)\Microsoft Visual Studio\Shared\Python36_64\python3.6
# _*_ coding:utf-8 _*_

from . import views
from django.conf.urls import url

urlpatterns = [
    url('^$', views.index),
    url(r'^(\d+)/$', views.detail),
    url(r'^grades/$',views.grades),
    url(r'^students/$', views.students),
    url(r'^addstudent/$', views.addStudent),
    url(r'^grades/(\d+)$', views.gradesStudents),
    url(r'^addstudent2/$', views.addStudent2),
    url(r'^students/(\d+)$', views.studentByPage),
    url(r'^studentsrearch/(\w+)$', views.studentSearch),
    url(r'^gradescmp$', views.gradesCmp),
    url(r'^gradesor$', views.gradesOR),
]

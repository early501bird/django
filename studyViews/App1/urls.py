# !c:\Program Files (x86)\Microsoft Visual Studio\Shared\Python36_64\python3.6
# _*_ coding:utf-8 _*_

from . import views
from django.conf.urls import url

urlpatterns = [
    url('^$', views.index),
    url(r'^attrib/$', views.Attribles),
    url(r'^get1/$', views.get1),  # http://127.0.0.1:8000/get1?a=12&b=132&c=53566
    url(r'^get2/$', views.get2),  # http://127.0.0.1:8000/get2?a=12&a=132&c=53566
    url(r'^showregist/$', views.showRegist),
    url(r'^showregist/regist/$', views.regist),
    url(r'^showresponse/$', views.showResponse),
    url(r'^cookietest/$', views.cookie),
    url(r'^redirect1/$', views.redirect1),
    url(r'^redirect2/$', views.redirect2),
    url(r'^main/$', views.main),
    url(r'^login/$', views.login),
    url(r"^showmain/$", views.showmain),
    url(r"^quit/$", views.quit),

]

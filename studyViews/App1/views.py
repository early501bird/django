from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse


def index(request):
    return HttpResponse("test view index")


def Attribles(request):
    print(request.path)
    print(request.method)
    print(request.encoding)
    print(request.GET)
    print(request.POST)
    print(request.FILES)
    print(request.COOKIES)
    print(request.session)
    return HttpResponse('attribles')


def get1(request):
    a = request.GET.get('a')
    b = request.GET['b']
    c = request.GET.get('c')
    return HttpResponse(a + " " + b + " " + c)


def get2(request):
    a = request.GET.getlist('a')
    a1 = a[0]
    a2 = a[1]
    c = request.GET['c']
    return HttpResponse(a1 + ' ' + a2 + " " + c)


def showRegist(request):
    return render(request, 'App1/regist.html')


def regist(request):
    name = request.POST.get("name")
    gender = request.POST.get('gender')
    age = request.POST.get('age')
    hobby = request.POST.getlist('hobby')
    return HttpResponse("name:{0},gender:{1},age:{2},hobby:{3}".format(name, gender, age, hobby))


def showResponse(request):
    res = HttpResponse()
    res.content = b'good luck'
    print('content:', res.content)
    print('chatset:', res.charset)
    print('status-code:', res.status_code)
    # print('content-type:',res.content-type)
    return res


# cookie
def cookie(request):
    res = HttpResponse()
    res.set_cookie("lie", "good ")
    cookie = request.COOKIES
    res.write("<h1>" + cookie['lie'] + "</h1>")
    return res


# HttpResponseRedirect

from django.http import HttpResponseRedirect
from django.shortcuts import redirect


def redirect1(request):
    # return HttpResponseRedirect('/redirect2')
    # 直接重定向redirect2视图中
    # HttpReponseRedirect简化形式
    return redirect('/redirect2')


def redirect2(request):
    return HttpResponse('this is httpResponse redirected page')


def main(request):
    username = request.session.get('name', "游客")
    return render(request, 'App1/main.html', {"username": username})


def login(request):
    return render(request, "App1/login.html")


def showmain(request):
    if request.GET:
        username = request.GET['username']
        request.session['name'] = username
        request.session.set_expiry(10)
        print('set session success:', username)
    return HttpResponseRedirect("/main")


from  django.contrib.auth import logout


def quit(request):
    logout(request)
    # request.session.flush()
    # request.session.clear()
    return redirect('/main')

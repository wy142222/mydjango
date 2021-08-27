import json

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect

# Create your views here.
# request, template_name, context=None(dict)
from django.urls import reverse

from login.models import LoginInfo


def index(request):
    # 路由是动态获取的.根据name=home,获取url
    path=reverse('home')
    print(path)
    userinfos=LoginInfo.objects.all()

    context={
        'userinfos':userinfos,
        '路径':path,
        'name':'如花'
    }

    return render(request,'index.html',context=context)

def detail(request,password,user):
    print(request)
    info=user+password

    return HttpResponse(info)

def get(request):
    # username=request.GET.get("user")
    password=request.GET['password']
    username1=request.GET.getlist("user")[0]
    username2 = request.GET.getlist("user")[1]
    print(username1,username2,password)

    return HttpResponse(username1+" "+ username2+password)
def post(request):
    '''重定向到指定网页'''
    # return  redirect("https://www.baidu.com/")
    '''重定向到首页'''
    path = reverse('home')
    return  redirect(path)

def set_cooking(request):
    username=request.GET.get("user")
    response=HttpResponse("set_cookie")
    response.set_cookie("username",username,max_age=60)
    return  response



from django.http import HttpResponse
from django.shortcuts import render
from .models import Users
import os
from LogWeb.settings import BASE_DIR

def regitsterview(request):
    return render(request,"Register.html")

def loginview(request):
    return render(request,"Login.html")

def login(request):         #登陆
    if request.is_ajax():
        name = request.POST.get("name")
        if not checkName(name):
            pwd = request.POST.get("password")
            user = Users.objects.get(name=name)
            if pwd == user.pwd:
                request.session["user_id"] = name
                return HttpResponse("登陆成功！")
            else:
                return HttpResponse("登陆失败！")
        else:
            return HttpResponse("用户不存在！")
    else:
        return HttpResponse("请求错误！")


def register(request):                  #注册
    if request.is_ajax():
        name = request.POST.get("name")
        if checkName(name):
            GENDER_CHOICE = { (0, '男'), (1, '女'), (2, '保密')}
            pwd = request.POST.get("password")
            gender = GENDER_CHOICE[request.POST.get("gender")]
            email = request.POST.get("email")
            phone = request.POST.get("phone")
            file_obj = request.FILES.get("imgfile")  # 获取文件对象
            file_name = file_obj.name                 # 获取文件名字
            path = os.path.join(BASE_DIR,"static","images", file_name)	# 拼接文件路径 TUT注意拼接正确...
            try:
                f = open(path, "wb")				#将上传文件对象写入文件并存储
                for line in file_obj:
                    f.write(line)
                user = Users(name=name, pwd=pwd, gender=gender, email=email, phone=phone,cover=path)
                user.save()
                return HttpResponse("注册成功！")
            except Exception as e:
                return HttpResponse("注册失败！")
        else:
            return HttpResponse("用户已存在！")
    return HttpResponse("请求错误！")

def checkName(name):            #检测用户名是否存在
    if Users.objects.filter(name=name).count() == 0 :
        return True
    else:
        return False


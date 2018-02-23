from django.http import HttpResponse
from django.shortcuts import render
from .models import Users
import os
from LogWeb.settings import BASE_DIR

def loginview(request):
    return render(request,"Register.html")

def login(request):
    pass

def register(request):
    # $formData.append("name",$("#name").val());
    # $formData.append("password",$("#pwd").val());
    # $formData.append("gender",$("input[name='radio']:checked").value);
    # $formData.append("email",$("#email").val());
    # $formData.append("phone",$("#phone").val());
    # $formData.append("imgfile",$("#file-up")[0].files[0]);
    if request.is_ajax():
        name = request.POST.get("name")
        pwd = request.POST.get("password")
        gender = request.POST.get("gender")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        file_obj = request.FILES.get("imgfile")  # 获取文件对象
        file_name = file_obj.name                 # 获取文件名字
        path = os.path.join(BASE_DIR,"static","file", file_name)	# 拼接文件路径 TUT注意拼接正确...
        try:
            f = open(path, "wb")				#将上传文件对象写入文件并存储
            for line in file_obj:
                f.write(line)
            user = Users(name=name, pwd=pwd, gender=gender, email=email, phone=phone,cover=path)
            user.save()
            return HttpResponse("注册成功！")
        except Exception as e:
            return HttpResponse("注册失败！")

    return HttpResponse("66！")
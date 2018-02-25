from django.shortcuts import render
from django.http import HttpResponse
from Log.models import Log,LogCategory
from Users.models import Users
from django.core import serializers
import json,datetime

def LogView(request):
    return render(request,"Log.html")

def getMyLogList(request):      #获取我的文章列表
    id = request.GET.get("id")
    page =  request.GET.get("page")
    pagesize =  request.GET.get("pagesize")
    content = {}
    result = Log.objects.filter(author=id).order_by("time")
    result = result[(page-1)*pagesize:page*pagesize]
    logs = []
    for log in result:
        new_log = {}
        new_log["id"] = log.pk
        new_log["title"] = log.title
        new_log["categary"] = log.category.name
        new_log["content"] = log.content
        logs.append(new_log)
    content["logs"] = logs
    return HttpResponse(json.dumps(content),content_type='application/json')

def getLogContent(request):     #获取指定id文章，并且文章点击量+1
    id = request.GET.get("id")
    result =[Log.objects.get(id = id)]
    result[0].hit += 1
    result[0].save()
    result = serializers.serialize("json",result)
    return HttpResponse(json.dumps(result),content_type='application/json')

def publishLogView(request):
    return render(request,"LogPublish.html")


def publishLog(request):        #添加文章
    title = request.POST.get("title")
    categary = request.POST.get("categary")
    content = request.POST.get("content")
    author = request.session["user_id"]
    try:
        log = Log.objects.create(
            title=title,
            category=LogCategory.objects.get(id=categary),
            content=content,
            author=Users.objects.get(id = author),  # 应该存在session里的
            time=datetime.datetime.now(),
        )
        log.save()
        return HttpResponse("注册成功！")
    except Exception as e:
        return HttpResponse(request.POST.get("categary"))

def deleteLog(request):         #删除文章
    id = request.GET.get("id")
    # id = 4
    try:
        Log.objects.filter(id=id).delete()
        return HttpResponse("删除成功！")
    except:
        return HttpResponse("删除失败！")

def updateLog(request):        #更新文章
    id = request.POST.get("id")
    title = request.POST.get("title")
    categary = request.POST.get("category")
    content = request.POST.get("content")
    author = request.session["user_id"]
    try:
        log = Log.objects.get(id = id)
        log.title = title
        log.categary = LogCategory.objects.get(id=categary)
        log.content = content
        log.author = Users.objects.get(id=author)
        log.save()
        return HttpResponse("更新成功！")
    except Exception as e:
        return HttpResponse("更新失败！")


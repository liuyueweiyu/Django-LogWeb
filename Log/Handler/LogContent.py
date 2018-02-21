from django.shortcuts import render
from django.http import HttpResponse
import json

def getLog(request):
    return render(request,"Log.html")

def getLogContent(request):
    id = request.GET.get("id")
    print(id)
    content = {}
    content["sss"] = id
    return HttpResponse(json.dumps(content),content_type='application/json')
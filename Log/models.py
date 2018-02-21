#-*- coding: UTF-8 -*-

from django.db import models
from Users.models import Users

# Create your models here.

class LogCategory(models.Model):            #文章分类
    name = models.CharField("分类名称",max_length=15)

class Log(models.Model):                    #文章
    title = models.CharField("标题",max_length=30)
    category = models.ForeignKey(LogCategory)
    content = models.TextField("内容",default='')
    time = models.DateTimeField("发布时间")
    author = models.ForeignKey(Users,default=1)
    hit  = models.IntegerField("点击量",default=0)
    like = models.IntegerField("点赞数",default=0)
    collect = models.IntegerField("收藏数",default=0)

class LogTag(models.Model):                 #文章tag
    name = models.CharField("名称",max_length=10)
    log = models.ForeignKey(Log)

class LogComment(models.Model):             #文章评论
    commet = models.CharField("评论",max_length=140)
    time = models.DateTimeField("评论时间")
    author = models.ForeignKey(Users,default=1)
    log = models.ForeignKey(Log)

class LogReply(models.Model):               #文章回复
    reply = models.CharField("回复",max_length= 140)
    time = models.DateTimeField("回复时间")
    comment = models.ForeignKey(LogComment)
    author = models.ForeignKey(Users,default=1)

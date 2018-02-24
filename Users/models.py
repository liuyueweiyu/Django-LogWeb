from django.db import models

# Create your models here.


class Users(models.Model):
    name = models.CharField("昵称",max_length=15)
    pwd = models.CharField("密码",max_length=20,default='123')
    gender = models.CharField("性别",max_length=2,default='未知')
    birthday = models.DateField("出生日期",default='1990-01-01')
    email = models.EmailField("邮箱地址",max_length=20)
    phone = models.CharField("电话号码",max_length=11)
    cover = models.CharField("头像",max_length=50,default="..")
    introduce = models.CharField("简介",max_length=140)

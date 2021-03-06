"""LogWeb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.views.static import serve
from django.contrib import admin
from django.conf import settings
from Log.Handler import LogContent
from Log.uploads import upload_image
from Users import User_Handler
# from Log import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r"^uploads/(?P<path>.*)$",serve, {"document_root": settings.MEDIA_ROOT, }),
    url(r'^upload/(?P<dir_name>[^/]+)$', upload_image, name='upload_image'),
    #

    url(r'^Log/',LogContent.LogView),
    url(r'^LogContent$',LogContent.getLogContent),
    url(r'^publishLogView$',LogContent.publishLogView),
    url(r'^puhlishLog/',LogContent.publishLog),
    url(r'^deleteLog',LogContent.deleteLog),
    url(r'^updateLog',LogContent.updateLog),
    url(r'^regitsterview',User_Handler.regitsterview),
    url(r'^register',User_Handler.register),
    url(r'^loginview', User_Handler.loginview),
    url(r'^login', User_Handler.login),

]

#### KindEditor在Django中配置

	##### 	Django-1.11.10

#####	KindEditor-4.1.11

1. KindEditor下载地址

   http://kindeditor.net/demo.php

2. 将kindeditor解压后配置后放置项目根目录static文件夹下

3. 在admin下配置

   1. 在setting.py中配置static路径

      ```python
      STATIC_URL = '/static/'
      HERE = os.path.dirname(os.path.abspath(__file__))
      HERE = os.path.join(HERE, '../')
      STATICFILES_DIRS = (
          # Put strings here, like "/home/html/static" or "C:/www/django/static".
          # Always use forward slashes, even on Windows.
          # Don't forget to use absolute paths, not relative paths.
          os.path.join(HERE, 'static/'),
      )
      ```

   2. 在kindEditor目录下创建conifg.js配置文件

      ```javascript
      //config.js
      KindEditor.ready(function(K) {
              // K.create('textarea[name=content]', {
              K.create('#id_content', {
                  width: '800px',
                  height: '200px',
              });
      });
      //这里的#id_content,或是name=content,是通过登录admin后，右击对应控件，选择审查元素获得的。
      ```

   3. 在admin.py对应的管理类中添加class Media,引入js文件

      ```python
      from .models import  Article
      class ArticleAdmin(admin.ModelAdmin):
          list_display = ['title']
          class Media:
              js = ('/static/js/kindeditor-4.1.10/kindeditor-all-min.js',
                    '/static/js/kindeditor-4.1.10/lang/zh-CN.js',
                    '/static/js/kindeditor-4.1.10/config.js')

      admin.site.register(Article,ArticleAdmin)
      ```

4. 在应用中配置

   1. 将kindeditor 的js文件引入到要做富文本编辑器的网页中

      ```html
      <script src="/static/kindeditor-4.1.11/kindeditor-all-min.js"></script>
      <script src="/static/kindeditor-4.1.11/lang/zh-CN.js"></script>
      <script src="/static/kindeditor-4.1.11/themes/default/default.css"></script>
      <script>
      	var editor
          KindEditor.ready(function (k) {
            editor = k.create('#editor_id',{
              resizeType:1,
              allowPreviewEmoticons : false,
              allowImageRemote : false,
              uploadJson : '/upload/kindeditor',
            });
          })
       </script>
      ```

   2. 在html的textarea 中加入一个id=editor_id ,这个就是富文本编辑框。

      ```html
      <textarea id="editor_id" name="content" style="height: 400px" >{{ text }}</textarea>
      <!--注意，获取富文本编辑器的值要用到4.1定义的editor变量，获取方法为editor.html()-->
      ```

   3. 在static文件夹下新建media文件夹，并在setting.py后增加

      ```python
      MEDIA_URL = '/static/media/'
      MEDIA_ROOT = os.path.join(BASE_DIR, "static/media")
      ```

   4. 在项目的urls配置文件中配置

      ```python
      from django.views.static import serve

      urlpatterns = [
      	url(r"^uploads/(?P<path>.*)$",serve, {"document_root": settings.MEDIA_ROOT, }),
      ]

      #Django1.10以前这样写
      #url(r"^uploads/(?P<path>.*)$", \ "django.views.static.serve", \ {"document_root": settings.MEDIA_ROOT,}),
      ```

   5. 在应用中创建uploads.py文件

      ```python
      from django.http import HttpResponse
      from django.conf import settings
      from django.views.decorators.csrf import csrf_exempt
      import os
      import uuid
      import json
      import datetime as dt

      @csrf_exempt
      def upload_image(request, dir_name):
          result = {"error": 1, "message": "上传出错"}
          files = request.FILES.get("imgFile", None)
          if files:
              result = image_upload(files, dir_name)
          return HttpResponse(json.dumps(result), content_type="application/json")
      # 目录创建

      def upload_generation_dir(dir_name):
          today = dt.datetime.today()
          dir_name = dir_name + '/%d/%d/' % (today.year, today.month)
          if not os.path.exists(settings.MEDIA_ROOT + dir_name):
              os.makedirs(settings.MEDIA_ROOT + dir_name)
          return dir_name

      # 图片上传
      def image_upload(files, dir_name):
          # 允许上传文件类型
          allow_suffix = ['jpg', 'png', 'jpeg', 'gif',
                          'bmp', 'zip', "swf", "flv",
                          "mp3", "wav", "wma", "wmv",
                          "mid", "avi", "mpg", "asf",
                          "rm", "rmvb", "doc", "docx",
                          "xls", "xlsx", "ppt", "htm",
                          "html", "txt", "zip", "rar",
                          "gz", "bz2"]
          file_suffix = files.name.split(".")[-1]
          if file_suffix not in allow_suffix:
              return {"error": 1, "message": "图片格式不正确"}
          relative_path_file = upload_generation_dir(dir_name)
          path = os.path.join(settings.MEDIA_ROOT, relative_path_file)
          if not os.path.exists(path):  # 如果目录不存在创建目录
              os.makedirs(path)
          file_name = str(uuid.uuid1()) + "." + file_suffix
          path_file = os.path.join(path, file_name)
          file_url = settings.MEDIA_URL + relative_path_file + file_name
          open(path_file, 'wb').write(files.file.read())
          return {"error": 0, "url": file_url}
      ```

   6. 在应用的urls.py中导入刚才写的视图文件uploads.py

      ```python
      from blog.uploads import upload_image
      urlpatterns = [
          url(r'^upload/(?P<dir_name>[^/]+)$', upload_image, name='upload_image'),
      ]
      ```

      ​
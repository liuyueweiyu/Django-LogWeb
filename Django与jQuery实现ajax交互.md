### Django与jQuery实现ajax交互

1. jQuery的引用

   在Django下html中对静态文件的配置

   在setting.py最后添加

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

2. ajax发送简单数据类型

   ```javascript
   	//GET方法
   	$.ajax({ 
             type: "GET",    
             url: "/Menu/",
             dataType: "JSON",
             async: true,
             data: {
             	host:host,
             	port:port
             },
             success: function(data) {
             		//执行的代码
             }
   	});
         
   	//POST
   	$.ajax({ 
             type: "POST",
             url: "/Menu/",
             dataType: "JSON",
             async: true,
             data: {
             	host:host,
             	port:port
             },
             //发送csrftoken，防止跨站请求伪造，不发送会出现403提示:
             //CSRF verification failed. Request aborted.
       	  headers:{"X-CSRFToken":$("[name='csrfmiddlewaretoken']").val()},
             success: function(data) {
             		//执行的代码
             }
       }); 
   ```

   后台处理代码

   ```python
   def ajax(request):
       print(request.POST)	#print(request.GET)
       content = {}
       #处理代码
       #......
       return HttpResponse(json.dumps(content),content_type='application/json')
   ```

3. ajax发送复杂数据类型

   即上传文件

   ```javascript
      	var $formData=new FormData();	//FormData是HTML5的新对象，注意兼容性
       $formData.append("name",$("#hhh").val());
       $formData.append("img_file",$("#file-up")[0].files[0]);

   	//POST
   	$.ajax({
   		type: "POST",
   		url: "/ajaxhhh/",
       	dataType: "JSON",
   	    async: true,
   	    data: $formData,
   	    contentType:false,
   	    processData:false,
   	    //发送csrftoken，防止跨站请求伪造，不发送会出现403提示:
   	    //CSRF verification failed. Request aborted.
   	    headers:{"X-CSRFToken":$("[name='csrfmiddlewaretoken']").val()},
   	    success: function(data) {
           	//执行的代码
   	        console.log(data)
   	    }
       });
   ```

   如果是直接form表单提交也可以，不过要在form添加enctype="multipart/form-data"属性

   ```python
   def ajaxfile(request):
       content = {}
       if request.is_ajax():
           name = request.POST.get("name")
           file_obj = request.FILES.get("img_file")  # 获取文件对象
           file_name = file_obj.name                 # 获取文件名字
           path = os.path.join(BASE_DIR,"static","file", file_name)	# 拼接文件路径 TUT注意拼接正确...
           try:
               f = open(path, "wb")				#将上传文件对象写入文件并存储
               for line in file_obj:
                   f.write(line)
           except Exception as e:
               pass
   	#content返回的内容自行处理
       return HttpResponse(json.dumps(content),content_type='application/json')
   ```

   ​


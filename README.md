# Introduction

# Walkthrough

# Requirement

Tool

Braintree : 支付

Sublime

# 004 Setup a previous project

从github repository拿到trydjango的git地址git@github.com:navicester/trydjango18course.git

或者https://github.com/codingforentrepreneurs/ecommerce-2

## 克隆基础项目
``` dos
>git clone git@github.com:navicester/trydjango18course.git
```
`virtualenv .` 试了一下不工作，还是回到父目录执行

## 安装request组件
``` dos
>pip install requests[security] 有时安装不成功
>pip freeze
```
> 
<pre>
cffi==1.8.3
cryptography==1.5.1
enum34==1.1.6
idna==2.1
ipaddress==1.0.17
ndg-httpsclient==0.4.2
pyasn1==0.1.9
pycparser==2.14
pyOpenSSL==16.1.0
requests==2.11.1
six==1.10.0
</pre>

``` python
>pip install -r requirements.txt
```

## 更新django到1.8版本
``` python
>pip install django==1.8.4
>pip install django-registration-redux  --upgrade
```

## 更新安装组件
``` python
>pip freeze > requirements.txt
```

## 删除老的数据库
``` dos
>rm db.sqlite3
```

## 数据库迁移
``` dos
>python manage.py migrate
```

## 创建超级用户
``` python
>python manage.py createsuperuser
```

# 005 Trydjano18 to ecommerce
将文件里的trydjango18全部替换成ecommerce2，并添加新的git repository

Trydjango18目录改成ecommerce2
``` dos
>rm -rf .git 切记
git init
git remote add origin git@github.com:navicester/ecommerce2course.git
git add .
git push -u origin master
```

# 006 Project Roadmap

# 007 Product App
添加Product application
- 创建app `python manage.py startapp *app_name*`
- 定义Product类 (Model)
- 在settings里的INSTALLED_APPS添加这个新加的APP
- 添加Admin接口

之后会实现各个子功能
- DetaiView
 - 008 定义ProductDetailView (View)
 - 009 添加ProductDetailView入口 (url)
 - 010 实现模板 (template)

- ListView
 - 011 添加ProductListView (View), 模板(template), 入口 (url)
 - 012 模板里添加直接访问Model实例的链接 (get_absolute_url)
 - 013 定制Model queryset (Model Manager)
- Variation
 - 014 定义Variation (model)，添加admin，更新Product模板添加Variation选项(template)
 - 015 Product保存时，如果没有型号，则添加一个默认型号 (Post Save)
- Product Vew Layout
 - 016 分为两列，左边(`col-sm-8`)显示title，description，右边显示Variation
 - 017 图片上传功能 (image)
 - 018 搜索功能 (search)
 - 019 库存显示功能，应用(ModelFormset)功能
 - 020 库存登录才能访问，(LoginRequiredMixin)
 - 021 消息 (Message)
 - 022 分享
 - 023 动态更新价格 (Jquery)


创建app
``` dos
>python manage.py startapp product
```

在products.models添加product类
``` python
from django.db import models

# Create your models here.
class Product(models.Model):
	title = models.CharField(max_length=120)
	description = models.TextField(blank=True, null=True)
	price = models.DecimalField(decimal_places=2, max_digits=20)
	active = models.BooleanField(default=True)

	def __unicode__(self): #def __str__(self):
		return self.title
```

settings里添加products
``` python
INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.sites',
    'django.contrib.staticfiles',
	'newsletter',
    'products',
    'crispy_forms',
    'registration',
)
```
数据库迁移
``` dos
>python manage.py makemigrations
>python manage.py migrate
```

添加admin接口. `products.admin.py`
``` python
from .models import Product

# Register your models here.
admin.site.register(Product)
```

# 008 Product Detail View
创建Product Detail View,包含
- 从DetailView继承，并设置model
- 指定template/context, 并渲染render

更新*products.views*，创建ProductDetailView，并指定template和context （测试用）
``` python
from django.views.generic.detail import DetailView
from .models import Product

# Create your views here.
class ProductDetailView(DetailView):
	model = Product

def product_detail_view_func(request, id):
	product_instance = Product.objects.get(id=id)

	template = "products/product_detail.html"
	context = {	
		"object": product_instance
	}
	return render(request, template, context)
```
http://127.0.0.1:8000/products/1/

## 参考
https://docs.djangoproject.com/en/1.8/ref/class-based-views/generic-display/#detailview

Generic display views
- DetailView
- ListView

**class django.views.generic.detail.DetailView**
<pre>
While this view is executing, self.object will contain the object that the view is operating upon.
This view inherits methods and attributes from the following views:

•	django.views.generic.detail.SingleObjectTemplateResponseMixin
•	django.views.generic.base.TemplateResponseMixin
•	django.views.generic.detail.BaseDetailView
•	django.views.generic.detail.SingleObjectMixin
•	django.views.generic.base.View

Method Flowchart
1.	dispatch()
2.	http_method_not_allowed()
3.	get_template_names()
4.	get_slug_field()
5.	get_queryset()
6.	get_object()
7.	get_context_object_name()
8.	get_context_data()
9.	get()
10.	render_to_response()
</pre>

**class django.views.generic.base.View**
<pre>
dispatch(request, *args, **kwargs)
	The view part of the view – the method that accepts a request argument plus arguments, and returns a HTTP response.
	The default implementation will inspect the HTTP method and attempt to delegate to a method that matches the HTTP method; a GET will be delegated to get(), a POST to post(), and so on.
	By default, a HEAD request will be delegated to get(). If you need to handle HEAD requests in a different way thanGET, you can override the head() method. See Supporting other HTTP methods for an example.

http_method_not_allowed(request, *args, **kwargs)
	If the view was called with a HTTP method it doesn’t support, this method is called instead.
	The default implementation returns HttpResponseNotAllowed with a list of allowed methods in plain text.
</pre>

class django.views.generic.base.TemplateResponseMixin
<pre>
get_template_names()
	Returns a list of template names to search for when rendering the template.
	If template_name is specified, the default implementation will return a list containing template_name (if it is specified).
render_to_response(context, **response_kwargs)¶
	Returns a self.response_class instance.
	If any keyword arguments are provided, they will be passed to the constructor of the response class.
	Calls get_template_names() to obtain the list of template names that will be searched looking for an existent template.
</pre>

class django.views.generic.detail.SingleObjectMixin
<pre>
get_slug_field()
	Returns the name of a slug field to be used to look up by slug. By default this simply returns the value of slug_field.
get_queryset()
	Returns the queryset that will be used to retrieve the object that this view will display. By default, get_queryset()returns the value of the queryset attribute if it is set, otherwise it constructs a QuerySet by calling the all()method on the model attribute’s default manager.
get_object(queryset=None)
	Returns the single object that this view will display. If queryset is provided, that queryset will be used as the source of objects; otherwise, get_queryset() will be used. get_object() looks for a pk_url_kwarg argument in the arguments to the view; if this argument is found, this method performs a primary-key based lookup using that value. If this argument is not found, it looks for a slug_url_kwarg argument, and performs a slug lookup using the slug_field.
get_context_object_name(obj)
	Return the context variable name that will be used to contain the data that this view is manipulating. Ifcontext_object_name is not set, the context name will be constructed from the model_name of the model that the queryset is composed from. For example, the model Article would have context object named 'article'.
get_context_data(**kwargs)
	Returns context data for displaying the list of objects.
	The base implementation of this method requires that the self.object attribute be set by the view (even if None). Be sure to do this if you are using this mixin without one of the built-in views that does so.
	It returns a dictionary with these contents:
	•	object: The object that this view is displaying (self.object).
	•	context_object_name: self.object will also be stored under the name returned byget_context_object_name(), which defaults to the lowercased version of the model name.
</pre>

[class django.views.generic.list.ListView](https://docs.djangoproject.com/en/1.8/ref/class-based-views/generic-display/#django.views.generic.list.ListView)
<pre>
A page representing a list of objects.
While this view is executing, self.object_list will contain the list of objects (usually, but not necessarily a queryset) that the view is operating upon.
Ancestors (MRO)
This view inherits methods and attributes from the following views:
•	django.views.generic.list.MultipleObjectTemplateResponseMixin
•	django.views.generic.base.TemplateResponseMixin
•	django.views.generic.list.BaseListView
•	django.views.generic.list.MultipleObjectMixin
•	django.views.generic.base.View

Method Flowchart
1.	dispatch()
2.	http_method_not_allowed()
3.	get_template_names()
4.	get_queryset()
5.	get_context_object_name()
6.	get_context_data()
7.	get()
8.	render_to_response()
</pre>

# 009 url with django app
实现DetailView的显示，其通过测试函数分解其功能

https://github.com/codingforentrepreneurs/Guides/blob/master/all/common_url_regex.md

在ecommerce2.url添加入口
``` python
    url(r'^products/', include('products.urls')),       
```

新建文件products.url
其中, `as_view`将class based view转换为function based view
`P<id>`这个跟view里面的参数是一致的
``` python
from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin

from .views import ProductDetailView

urlpatterns = [
    # Examples:
    url(r'^(?P<pk>\d+)/$', ProductDetailView.as_view(), name='product_detail'),
    #url(r'^(?P<id>\d+)', 'products.views.product_detail_view_func', name='product_detail_function'),
]
```

# 010 Add html templates
创建*products/templates/products/product_detail.htnl*

DetailView的默认名字是`template_name = "<appname>/<modelname>_detail.html"`

可以通过更新这个名字来修改template位置

http://127.0.0.1:8000/products/1/
可以访问刚刚创建的product

如果访问的数据越界了，需要做一些处理
``` python
-from django.shortcuts import render
+from django.shortcuts import render, get_object_or_404
+from django.http import Http404

def product_detail_view_func(request, id):
-    product_instance = Product.objects.get(id=id)
+	product_instance = get_object_or_404(Product, id=id)
+	try:
		product_instance = Product.objects.get(id=id)
+	except Product.DoesNotExist:
+		raise Http404
+	except:
+		raise Http404

	template = "products/product_detail.html"
	context = {	
		"object": product_instance
	}

	return render(request, template, context)
```

# 011 ListView
https://docs.djangoproject.com/en/1.8/ref/class-based-views/generic-display/#listview

ProductListView实现
- 添加入口 (url), **ListView.as_view()
- 添加ProductListView，从ListView继承
- 添加模板

更新products.urls
``` python
-from .views import ProductDetailView
+from .views import ProductDetailView, ProductListView

urlpatterns = [
    # Examples:
+    url(r'^$', ProductListView.as_view(), name='products'),
]
```
访问地址
http://127.0.0.1:8000/products/

更新products.views，添加listview的处理
``` python
from django.views.generic.list import ListView
from django.utils import timezone

class ProductListView(ListView):
    model = Product

    def get_context_data(self, *args, **kwargs):
        context = super(ProductListView, self).get_context_data(*args, **kwargs)
        context["now"] = timezone.now()
        return context
```

添加*products/templates/products/product_list.html*
``` html
{% extends "base.html" %}

{% block content %}

<table>
	{% for object in object_list %}
	<tr>
		<td>{{object.title}}</td>
	</tr>
	{% endfor %}

</table>
{% endblock %}
```

# 012 Using Links for Model Instance

实现：模板里添加直接访问Model实例的链接 (get_absolute_url)

*Products/templates/products/product_list.html*
``` html
<td><a href="/products/{{object.pk}}/">{{object.title}}</a></td>
<td><a href="{% url 'product_detail' pk=object.pk %}">{{object.title}}</a></td>
```

可以用下面的方式
``` html
<td><a href="{{ object.get_absolute_url }}">{{object.title}}</a></td>
```

更新models
``` python
from django.core.urlresolvers import reverse

class Product(models.Model):

	def get_absolute_url(self):
		return reverse("product_detail", kwargs={"pk": self.pk})
```

# 013 Model Manager

实现：定制化model queryset, 过滤model里面的一些objects

https://docs.djangoproject.com/en/1.10/topics/db/managers/

Model里添加Model Manager
``` python
class ProductQuerySet(models.query.QuerySet):
	def active(self):
		return self.filter(active=True)


class ProductManager(models.Manager):
	def get_queryset(self):
		return ProductQuerySet(self.model, using=self._db)

	def all(self, *args, **kwargs):
		return self.get_queryset().active()

class Product(models.Model):
	title = models.CharField(max_length=120)
	description = models.TextField(blank=True, null=True)
	price = models.DecimalField(decimal_places=2, max_digits=20)
	active = models.BooleanField(default=True)

+	objects = ProductManager()
```

view里更新queryset
``` python
class ProductListView(ListView):
    model = Product
+    queryset = Product.objects.all()
```

# 014 Product Variation
实现：添加产品型号
- 定义Variation (model)
- 添加admin接口
- 更新模板，添加Variation选项

添加类variation，文件products.models
``` python
class Variation(models.Model):
	product = models.ForeignKey(Product)
	title = models.CharField(max_length=120)
	price = models.DecimalField(decimal_places=2, max_digits=20)
	sale_price = models.DecimalField(decimal_places=2, max_digits=20, null=True, blank=True)
	active = models.BooleanField(default=True)
	inventory = models.IntegerField(null=True, blank=True) #refer none == unlimited amount

	def __unicode__(self):
		return self.title

	def get_price(self):
		if self.sale_price is not None:
			return self.sale_price
		else:
			return self.price

	def get_absolute_url(self):
		return self.product.get_absolute_url()
```

添加admin接口
``` python
from .models import Variation
admin.site.register(Variation)
```

更新ProductDetail
``` html
<select class='form-control'>
	{% for vari_obj in object.variation_set.all %}
	<option value = "{{vari_obj.id}}">
		{{vari_obj}}
	</option>
	{% endfor %}
</select>
```

更新一些css符合commerce的风格

# 015 Post Save Signal for Variation
https://docs.djangoproject.com/en/1.8/ref/signals/#post-save

实现：Post Save，新建一个product时，如果没有variation，那么创建一个default的variation

如果产品保存是没有型号variation，则自动创建一个

在model添加post save处理
新建一个product时，如果没有variation，那么创建一个default的variation
``` python
def product_post_saved_receiver(sender, instance, created, *args, **kwargs):
	product = instance
	variations = product.variation_set.all()
	if variations.count() == 0:
		new_var = Variation()
		new_var.product = product
		new_var.title = "Default"
		new_var.price = product.price
		new_var.save()

post_save.connect(product_post_saved_receiver, sender=Product)
```

在*template product_detail.html*过滤掉默认创建的variation
``` html
+{% if object.variation_set.count > 0 %}
	<select class='form-control'>    
		{% for vari_obj in object.variation_set.all %}
		<option value = "{{vari_obj.id}}">
			{{vari_obj}}
		</option>
		{% endfor %}
	</select>
+{% endif %}
<br/>
+<a href="#">Add to Cart</a>
```

# 016 Project Detail Layout
实现：分为两栏，左边是描述，右边是Variation
``` html
+<div class="row">
+	<div class="col-sm-8"> 
		<h2>{{object.title}}</h2>
+		<p class="lead">
+			{{object.description}}
+		</p>
+	</div>

+<div class="col-sm-4">
+	<h3>{{object.price}}</h3>
	{% if object.variation_set.count > 1 %}
		<select class='form-control'>    
			{% for vari_obj in object.variation_set.all %}
			<option value = "{{vari_obj.id}}">
				{{vari_obj}}
			</option>
			{% endfor %}
		</select>
	{% endif %}
	<br/>
	<hr/>
+	<h4>Related Products</h4>
	<a href="#">Add to Cart</a>
+</div>
{% endblock %}
```

# 017 Image Uploads

https://github.com/codingforentrepreneurs/Guides/blob/master/all/imagefield_and_pillow.md

实现：图片上传功能

pillow是python image库
``` dos
>pip install pillow
```

创建ProductImage类 (product.models)

其中，存放路径在MEDIA_ROOT = os.path.join(os.path.dirname(BASE_DIR), "static_in_env", "media_root")

子目录可以自定义

这儿有2个文件iphone_cover.jpg，mp3_player.jpg分别传给Product里面的iPhone Cover和MP3 Player
``` python
from django.utils.text import slugify

def image_upload_to(instance, filename):
	title = instance.product.title
	slug = slugify(title)
	basename, file_extension = filename.split(".")
	new_filename = "%s-%s.%s" %(slug, instance.id, file_extension)
	return "products/%s/%s" %(slug, new_filename)
```

比如上传的文件名名为iphone_cover.jpg，为iPhone Cover model添加ProductImage

则title, slug, basename, file_extension, new_filename的值分别如下：

[iPhone Cover] [iphone-cover] [iphone_cover] [jpg] [iphone-cover-2.jpg]
<pre>
如果是第一次创建ProductImage，instance.id为None
MP3 Player mp3-player mp3_player jpg mp3-player-None.jpg
MP3 Player mp3_player.jpg
同样的名字，如果做第二次修改
MP3 Player mp3-player mp3_player jpg mp3-player-3.jpg
MP3 Player mp3_player.jpg
Currently: products/mp3-player/mp3-player-3.jpg 
同样的名字，如果继续覆盖，文件不会被覆盖，而是增加随机数重新拷贝一个
MP3 Player mp3-player mp3_player jpg mp3-player-3.jpg
MP3 Player mp3_player.jpg
Currently: products/mp3-player/mp3-player-3_7KveE47.jpg 
</pre>

入参instance和filename分别为
iPhone Cover iphone_cover.jpg
filename为上传文件的文件名
``` python
class ProductImage(models.Model):
	product = models.ForeignKey(Product)
	image = models.ImageField(upload_to=image_upload_to)

	def __unicode__(self):
		return self.product.title
```

``` dos
>python manage.py makemigrations
>python manage.py migrate
```

创建admin接口
``` python
from .models import Product,Variation,ProductImage

admin.site.register(ProductImage)
```

在product_detail_view添加图片显示

下面这两个的显示分别如下
> 
<pre>
			{{ img.image.file }}
			{{ img.image.url }}
</pre>
结果为:
> 
<pre>
D:\virtualenv\ecommerce-ws\src\static_in_env\media_root\products\mp3-player\mp3-player-None.jpg 
/media/products/mp3-player/mp3-player-None.jpg
</pre>

``` python
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(os.path.dirname(BASE_DIR), "static_in_env", "media_root")
```




















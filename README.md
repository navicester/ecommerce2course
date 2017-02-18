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
While this view is executing, `self.object` will contain the object that the view is operating upon.
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
get_slug_field()¶
Returns the name of a slug field to be used to look up by slug. By default this simply returns the value of slug_field.
get_queryset()¶
Returns the queryset that will be used to retrieve the object that this view will display. By default, get_queryset()returns the value of the queryset attribute if it is set, otherwise it constructs a QuerySet by calling the all()method on the model attribute’s default manager.
get_object(queryset=None)¶
Returns the single object that this view will display. If queryset is provided, that queryset will be used as the source of objects; otherwise, get_queryset() will be used. get_object() looks for a pk_url_kwarg argument in the arguments to the view; if this argument is found, this method performs a primary-key based lookup using that value. If this argument is not found, it looks for a slug_url_kwarg argument, and performs a slug lookup using the slug_field.
get_context_object_name(obj)¶
Return the context variable name that will be used to contain the data that this view is manipulating. Ifcontext_object_name is not set, the context name will be constructed from the model_name of the model that the queryset is composed from. For example, the model Article would have context object named 'article'.
get_context_data(**kwargs)¶
Returns context data for displaying the list of objects.
The base implementation of this method requires that the self.object attribute be set by the view (even if None). Be sure to do this if you are using this mixin without one of the built-in views that does so.
It returns a dictionary with these contents:
•	object: The object that this view is displaying (self.object).
•	context_object_name: self.object will also be stored under the name returned byget_context_object_name(), which defaults to the lowercased version of the model name.
</pre>

class django.views.generic.list.ListView¶
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












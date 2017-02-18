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

更新products.views，创建ProductDetailView，并指定template和context （测试用）
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
While this view is executing, `self.object` will contain the object that the view is operating upon.
This view inherits methods and attributes from the following views:
•	django.views.generic.detail.SingleObjectTemplateResponseMixin
•	django.views.generic.base.TemplateResponseMixin
•	django.views.generic.detail.BaseDetailView
•	django.views.generic.detail.SingleObjectMixin
•	django.views.generic.base.View












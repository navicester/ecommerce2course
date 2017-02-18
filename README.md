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












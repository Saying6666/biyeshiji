from django.shortcuts import redirect, render

# Create your views here.
#frontend/views.py
from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import redirect, render

def home(request):
    return render(request, 'home.html')

def login(request):#登录
    print(request.method)
    if request.method == 'POST':#如果是post请求
        #form = AuthenticationForm(data=request.POST)#获取表单数据
        print(request.POST)
        #if form.is_valid():#如果表单数据有效
         #   return redirect('home')#重定向到主页
    
    return render(request, 'login.html', {'form': AuthenticationForm()})#返回登录页面

def index(request):
    return render(request, 'index.html');

def register(request):
    return render(request, 'register.html');
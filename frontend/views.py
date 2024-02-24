from django.conf import UserSettingsHolder
from django.http import JsonResponse
from django.shortcuts import redirect, render

# Create your views here.
#frontend/views.py
from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import redirect, render
from django.views.decorators.http import require_http_methods
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

@login_required
def home(request):
    return render(request, 'home.html')

def logout_view(request):
    logout(request)
    return redirect('login_view')

def login_view(request):#登录
    print(request.POST)
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user=authenticate(request,username=username, password=password)
        if user is not None:
            print('登录成功')
            login(request, user)
            print('登录成功2')
            return JsonResponse({'code': 0, 'msg': '登录成功'})#登录成功返回主页
        else:
            return render(request, 'login.html', {'error': '用户名或密码错误'})
    else:
     return render(request, 'login.html')

def index(request):
    return render(request, 'index.html');


def register(request):
    print(request.POST)
    email = request.POST.get('email')
    password = request.POST.get('password')
    if not email or not password:
        return render(request, 'register.html', {'error': '邮箱或密码不能为空'})

    # 判断邮箱是否已经注册
    if User.objects.filter(email=email).exists():
        print('邮箱已经注册')
        return JsonResponse({'code': 1, 'msg': '邮箱已经注册'})

    user = User.objects.create_user(username=email, email=email, password=password)
    user.save()

    user = authenticate(username=email, password=password)
    if user is not None:
        login_view(request)

    

    return JsonResponse({'code': 0, 'msg': '注册成功'})#注册成功返回主页
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect

from ai_apps.forms import LoginForm

from ai_apps.models import Users
def login_page(request):
    loginForm = LoginForm()
    return render(request, 'ai_apps_login.html',{"loginForm":loginForm })

def login_view(request):
    if request.method == 'GET':
        loginForm = LoginForm()
        return render(request, 'ai_apps_login.html',{"loginForm":loginForm })

    loginForm = LoginForm(data=request.POST)
    if not loginForm.is_valid():
        return render(request, 'ai_apps_login.html',{"loginForm":loginForm })
    # 此处注意cleaned_data，只有在is_valid()后才能使用
    data_dict = loginForm.cleaned_data
    username = request.POST['username']
    user = Users.objects.filter(**data_dict).first()

    if user:
        request.session['user_id'] = user.id
        request.session['username'] = username
        # 重定向到index
        return redirect('index')
    else:
        # 返回一个无效的登录错误消息。
        msg = "用户吗或密码错误"
        return render(request, 'ai_apps_login.html', {"loginForm": loginForm, "error": msg})



from django.shortcuts import render, redirect
from django.http import HttpResponse

def ars2048b_apps(request):
    if request.path == "/pknight_docs/ars2048b/apps/win/":
        return HttpResponse(render(request, 'ars2048b_app_win.html'))
    else:
        print(request.path)
        return HttpResponse("Invalid app type.", status=400)


def ars2048b_doc(request):
    # 将render返回的HttpResponse对象赋值给response
    response = HttpResponse(render(request, 'ars2048b_doc.html'))
     # 设置响应头，不缓存
    response['Cache-Control'] = 'no-cache' #针对浏览器端
    response['X-Accel-Buffering'] = 'no'  #针对nginx服务器端
    return response


from django.http import HttpResponse
from django.shortcuts import render


def how_to_process_an_order(request):
    # 将render返回的HttpResponse对象赋值给response
    response = HttpResponse(render(request, 'how_to_process_an_order.html'))
     # 设置响应头，不缓存
    response['Cache-Control'] = 'no-cache' #针对浏览器端
    response['X-Accel-Buffering'] = 'no'  #针对nginx服务器端
    return response
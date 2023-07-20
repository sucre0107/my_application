
from django.shortcuts import render, redirect
from django.http import HttpResponse

def usbelf_apps(request, app_type):
    if app_type == "win":
        return HttpResponse(render(request, 'usbelf_app_win.html', {"app_type": app_type}))
    elif app_type == "apple":
        return redirect("https://qrco.de/USBelf-for-ios")
    elif app_type == "android":
        return HttpResponse(render(request, 'usbelf_app_android.html', {"app_type": app_type}))
    else:
        return HttpResponse("Invalid app type.", status=400)


def usbelf_doc(request):
    # 将render返回的HttpResponse对象赋值给response
    response = HttpResponse(render(request, 'usbelf_doc.html'))
     # 设置响应头，不缓存
    response['Cache-Control'] = 'no-cache' #针对浏览器端
    response['X-Accel-Buffering'] = 'no'  #针对nginx服务器端
    return response

def usbelf_apple(request):
    # 将render返回的HttpResponse对象赋值给response
    response = HttpResponse(render(request, 'usbelf_doc_for_apple.html'))
     # 设置响应头，不缓存
    response['Cache-Control'] = 'no-cache' #针对浏览器端
    response['X-Accel-Buffering'] = 'no'  #针对nginx服务器端
    return response

def usbelf_android(request):
    # 将render返回的HttpResponse对象赋值给response
    response = HttpResponse(render(request, 'usbelf_doc_for_android.html'))
     # 设置响应头，不缓存
    response['Cache-Control'] = 'no-cache' #针对浏览器端
    response['X-Accel-Buffering'] = 'no'  #针对nginx服务器端
    return response
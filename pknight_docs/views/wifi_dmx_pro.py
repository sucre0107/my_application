
from django.shortcuts import render, redirect
from django.http import HttpResponse

def wifi_dmx_pro_apps(request):
    path_list = ''
    if request.path == "/pknight_docs/wifidmxpro/apps/android/":
        return HttpResponse(render(request, 'wifi_dmx_pro.html'))
    else:
        print(request.path)
        return HttpResponse("Invalid app type.", status=400)

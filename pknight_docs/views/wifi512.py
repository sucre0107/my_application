
from django.shortcuts import render, redirect
from django.http import HttpResponse

def wifi512_apps(request):
    path_list = ''
    if request.path == "/pknight_docs/wifi512/apps/android/":
        return HttpResponse(render(request, 'wifi512_app_android.html'))
    else:
        print(request.path)
        return HttpResponse("Invalid app type.", status=400)

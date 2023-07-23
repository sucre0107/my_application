"""
URL configuration for my_application project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from pknight_docs.views import index, usbelf, ars2048b
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
                  path("", index.index, name="pknight_doc_index"),
                  path("usbelf/", usbelf.usbelf_doc, name="pknight_doc_usbelf"),
                  path("usbelf/apple/", usbelf.usbelf_apple, name="pknight_doc_usbelf_apple"),
                  path("usbelf/android/", usbelf.usbelf_android, name="pknight_doc_usbelf_android"),
                  # path('usbelf/apps/<str:app_type>/', usbelf.usbelf_apps),  # 用于处理usbelf的app下载页面，这里不好命名我不使用
                  path('usbelf/apps/win/', usbelf.usbelf_apps, name="usbelf_app_win"),
                  path('usbelf/apps/apple/', usbelf.usbelf_apps, name="usbelf_app_apple"),
                  path('usbelf/apps/android/', usbelf.usbelf_apps, name="usbelf_app_android"),
                  path('ars2048b/', ars2048b.ars2048b_doc, name='pknight_doc_ars2048b'),
                  path('ars2048b/apps/win/', ars2048b.ars2048b_apps, name="ars2048b_app_win"),

              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

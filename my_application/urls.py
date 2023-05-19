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
from django.conf import settings
from django.conf.urls.static import static
from my_application import views
# path 必须是相对路径，否则会报错
urlpatterns = [
    path("pknight/admin/", admin.site.urls),
    path("pknight/ai_apps/", include("ai_apps.urls")),
    path("pknight/pknight_docs/", include("pknight_docs.urls")),
    path("pknight/pknight/", views.pknight, name="pknight"),

]  + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

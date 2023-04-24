from django.conf.urls.static import static
from django.urls import path
from simple_translation_application import views
from django.conf import settings

urlpatterns = [
    path("",views.index, name="index"),
    path("translate/",views.translate, name="translate"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
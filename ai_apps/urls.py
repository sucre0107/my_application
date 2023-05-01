from django.conf.urls.static import static
from django.urls import path
from ai_apps import views
from django.conf import settings

urlpatterns = [
    path("trans",views.translator, name="translator"),
    path("translate/",views.translate, name="translate"),
    path("stream_data/",views.stream_data, name="stream_data"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
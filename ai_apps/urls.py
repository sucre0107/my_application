from django.conf.urls.static import static
from django.urls import path
from ai_apps import views
from django.conf import settings
from utils import demo

urlpatterns = [
                  path("", views.index, name="index"),
                  # ------------测试------------#
                  #path('stream/', views.test_stream, name='test_stream'),
                path('stream/home/', views.home, name='home'),
                    path('stream/event/', views.event_stream_pack, name='event_stream_pack'),
                  # ------------测试------------#
                  path("trans/", views.translator, name="translator"),
                  path("trans/translate/", views.translate, name="translate"),
                  path("email/", views.email_writer, name="email_writer"),
                  path("email/generate/", views.generate_email, name="generate_email")
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

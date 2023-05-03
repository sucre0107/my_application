from django.conf.urls.static import static
from django.urls import path
from ai_apps import views
from django.conf import settings

urlpatterns = [
    path("trans/",views.translator, name="translator"),
    path("trans/translate/",views.translate, name="translate"),
    path("email/",views.email_writer, name="email_writer"),
    path("email/generate/",views.generate_email, name="generate_email")
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
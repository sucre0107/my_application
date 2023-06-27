from django.conf.urls.static import static
from django.urls import path
from ai_apps import views
from ai_apps.views import translator, index, email, customer_service_assistant
from django.conf import settings

urlpatterns = [
                  path("", index.index, name="index"),
                  path("trans/", translator.translator, name="translator"),
                  path("trans/translate/", translator.pack_trans_stream, name="pack_trans_stream"),
                  path("email/", email.email_writer, name="email_writer"),
                  path("email/generate/", email.pack_email_stream, name="pack_email_stream"),
                  path("csa/", customer_service_assistant.customer_service_assistant, name="csa"),
                  path("csa/generate/", customer_service_assistant.pack_reply_stream, name="pack_reply_stream"),
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

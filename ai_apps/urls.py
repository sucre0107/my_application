from django.conf.urls.static import static
from django.urls import path
from ai_apps import views
from ai_apps.views import translator, index, email, customer_service_assistant, chatbot, auth
from django.conf import settings

urlpatterns = [
                  # 登陆注册相关
                  path("auth/register/manual", auth.register_manual, name="register_manual"),
                  path('auth/', auth.login_page, name='login_page'),
                  path('auth/login/', auth.login_view, name='login'),

                  path("", index.index, name="index"),
                  # 翻译助手相关
                  path("trans/", translator.translator, name="translator"),
                  path("trans/translate/", translator.pack_trans_stream, name="pack_trans_stream"),
                  # 邮件助手相关
                  path("email/", email.email_writer, name="email_writer"),
                  path("email/generate/", email.pack_email_stream, name="pack_email_stream"),
                  # 客服助手相关
                  path("csa/", customer_service_assistant.customer_service_assistant, name="csa"),
                  path("csa/generate/", customer_service_assistant.pack_reply_stream, name="pack_reply_stream"),
                  # 聊天机器人相关
                  path("chatbot/", chatbot.chatbot, name="chatbot"),
                  path("chatbot/generate/", chatbot.pack_chatbot_stream, name="pack_chatbot_stream"),
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

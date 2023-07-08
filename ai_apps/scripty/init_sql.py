import os
import sys
import django
from ai_apps.utils.encrypt import md5



base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) # 获取当前文件的上上级目录，这里就是项目的根目录
sys.path.append(base_dir)  # 将项目的根目录添加到环境变量中
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "my_application.settings")  # 设置环境变量
django.setup() # 加载项目的配置，初始化django，这样才能使用django的ORM

from ai_apps.models import Users

# 建立一条管理员的数据
#Administrator.objects.create(username='admin111', password=md5('123456'),active=1,mobile='15088870679')
#建立一条用户的数据
Users.objects.create(username='sucreqiu_ai_apps', password=md5('PxUFcK!&$P2T'))
print("ok")
import pymysql
print(pymysql.__version__)



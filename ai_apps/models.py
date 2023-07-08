from django.db import models

# Create your models here.

class Users(models.Model):
    """ 用户 """
    username = models.CharField(verbose_name="用户名", max_length=32, db_index=True)
    password = models.CharField(verbose_name="密码", max_length=64)

    class Meta:
        verbose_name = "用户表"
        db_table = "users"


# _*_ coding:utf-8 _*_
from django.db import models
from datetime import datetime

from django.contrib.auth.models import AbstractUser
# Create your models here.




class User(models.Model):
    user_id = models.CharField(max_length=10, primary_key=True, verbose_name=u"帐号")
    password = models.CharField(max_length=20, verbose_name=u"密码")
    type = models.CharField(max_length=10, choices=(("administrator", u"管理员"), ("expert", u"专家")),
                            verbose_name=u"用户类型", default="expert")

    class Meta:
        verbose_name = u"用户信息表"
        verbose_name_plural = verbose_name
        db_table = "account_message"


class UserProfile(AbstractUser):
    type = models.CharField(max_length=15, choices=(("administrator", u"管理员"), ("expert", u"专家")),
                           verbose_name=u"用户类型", default="expert")

    class Meta:
        verbose_name = u"用户信息"
        verbose_name_plural = verbose_name
        db_table = "account"

    def __unicode__(self):
        return self.username


class EmailVerifyRecord(models.Model):
    code = models.CharField(max_length=20, verbose_name=u"验证码")
    email = models.EmailField(max_length=50, verbose_name=u"邮箱")
    send_type = models.CharField(choices=(("register", u"注册"), ("forget", u"找回密码")), max_length=10)
    send_time = models.DateField(default=datetime.now)

    class Meta:
        verbose_name = u"邮箱验证码"
        verbose_name_plural = verbose_name


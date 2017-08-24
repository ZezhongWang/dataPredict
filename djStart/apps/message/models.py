# _*_ coding:utf-8 _*_
from django.db import models
from datetime import datetime

from django.contrib.auth.models import AbstractUser
# Create your models here.


class UserProfile(AbstractUser):
    type = models.CharField(max_length=15, choices=(("administrator", u"管理员"), ("expert", u"专家")),
                           verbose_name=u"用户类型", default="expert")
    username = models.CharField(max_length=15, primary_key=True)
    id = models.CharField(max_length=10, default='default')

    class Meta:
        verbose_name = u"用户信息"
        verbose_name_plural = verbose_name
        db_table = "account"

    def __unicode__(self):
        return self.username


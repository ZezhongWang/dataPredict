# _*_ coding:utf-8 _*_
from django.db import models

from apps.message.models import User
# Create your models here.


class Expert(models.Model):
    # account_id = models.CharField(max_length=8, verbose_name=u"帐号", primary_key=True)
    account_id = models.ForeignKey('message.UserProfile', primary_key=True, verbose_name=u"用户帐号", on_delete=models.CASCADE)
    expert_number = models.CharField(max_length=8, verbose_name=u"专家证书编号", null=True, blank=True)
    valid_time = models.DateField(verbose_name=u"证书有效时间", null=True, blank=True)
    name = models.CharField(max_length=20, verbose_name=u"证书有效时间", null=True, blank=True)
    gender = models.CharField(max_length=10, choices=(("male", u"男"), ("female", u"女")), default="male")
    birthday = models.DateField(verbose_name=u"出生日期")
    politic = models.CharField(max_length=20, verbose_name=u"政治面貌")
    certificate_type = models.CharField(max_length=20, verbose_name=u"证件类型")
    certificate_number = models.CharField(max_length=20, verbose_name=u"证件号", null=True, blank=True)
    phone_number = models.CharField(max_length=20, verbose_name=u"电话号码", null=True, blank=True)
    email = models.EmailField(max_length=20, verbose_name=u"邮箱", null=True, blank=True)
    pic = models.ImageField(upload_to="image/%Y/%m", default="image/default/", max_length=100, verbose_name=u"照片")

    class Meta:
        verbose_name = u"专家信息表"
        verbose_name_plural = verbose_name
        db_table = "Expert"

# _*_ coding:utf-8 _*_
from django.db import models

from apps.message.models import UserProfile

# Create your models here.


class Expert(models.Model):
    # username = models.ForeignKey(UserProfile, primary_key=True, verbose_name=u"用户帐号", on_delete=models.CASCADE)
    username = models.OneToOneField(UserProfile, primary_key=True, verbose_name=u"用户帐号",
                                    on_delete=models.CASCADE, db_column='username')
    expert_number = models.CharField(max_length=8, verbose_name=u"专家证书编号", null=True, blank=True)
    valid_time = models.CharField(verbose_name=u"证书有效时间", null=True, blank=True, max_length=11)
    name = models.CharField(max_length=20, verbose_name=u"姓名", null=True, blank=True)
    gender = models.CharField(max_length=10, verbose_name=u"性别", choices=(("male", u"男"), ("female", u"女"))
                              , default="male", null=True, blank=True)
    birthday = models.CharField(verbose_name=u"出生日期", null=True, blank=True, max_length=11)
    politic = models.CharField(max_length=20, verbose_name=u"政治面貌", null=True, blank=True)
    certificate_type = models.CharField(max_length=20, choices=(("i.d.card", u"身份证"), ("student card", u"学生证")
                                                                , ("passport", u"学生证")), verbose_name=u"证件类型"
                                                                , default="i.d.card", null=True, blank=True)
    certificate_number = models.CharField(max_length=20, verbose_name=u"证件号", null=True, blank=True)
    phone_number = models.CharField(max_length=20, verbose_name=u"电话号码", null=True, blank=True)
    email = models.EmailField(max_length=20, verbose_name=u"邮箱", null=True, blank=True)
    picture = models.ImageField(upload_to="image/%Y/%m", default="image/default/", max_length=100, verbose_name=u"照片"
                                ,null=True, blank=True)
    state = models.CharField(max_length=10, choices=(("undo", u"待填表"), ("done", u"待审核"), ("denied", u"驳回申请"),
                                                    ("checked", u"已审核")), default="undo", null=True, blank=True)

    class Meta:
        verbose_name = u"专家信息表"
        verbose_name_plural = verbose_name
        db_table = "Expert"

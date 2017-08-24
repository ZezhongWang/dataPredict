# _*_ coding:utf-8 _*_
__author__ = 'w2w'
__date__ = '17-7-17 上午11:42'

from django import forms
from apps.expert.models import Expert
import re
from captcha.fields import CaptchaField


class ExpertForm(forms.ModelForm):
    class Meta:
        model = Expert
        fields = ['expert_number', 'valid_time', 'name', 'state',
                  'gender', 'birthday', 'politic', 'certificate_type',
                  'certificate_number', 'phone_number', 'email', 'picture']


class ResetForm(forms.Form):
    password_before = forms.CharField(required=True)
    password_after = forms.CharField(required=True)
    password_again = forms.CharField(required=True)
    captcha = CaptchaField(error_messages={"invalid": u"验证码错误"})


    # def clean_phone_number(self):
    #     phone_number = self.cleaned_data['phone_number']
    #     regex_phone_number = "^1[358]\d{9}$|^147\d{8}$|^176\d{8}$"
    #     p = re.compile(regex_phone_number)
    #     if p.match(phone_number):
    #         return phone_number
    #     else:
    #         raise forms.ValidationError(u"手机号码非法", code="mobile_invalid")
    #
    # def clean_birthday(self):
    #     birthday = self.cleaned_data['birthday']
    #     regex_birthday = "^\d{4}-\d{1,2}-\d{1,2}$|^d{4}/\d{1,2}/\d{1,2}$|^d{4}年\d{1,2}月\d{1,2}"
    #     p = re.compile(regex_birthday)
    #     if p.match(birthday):
    #         return birthday
    #     else:
    #         raise forms.ValidationError(u"出生日期格式错误", code="birthday_invalid")
    #
    # def clean_valid_time(self):
    #     valid_time = self.cleaned_data['valid_time']
    #     regex_valid_time = "^\d{4}-\d{1,2}-\d{1,2}$|^d{4}/\d{1,2}/\d{1,2}$|^d{4}年\d{1,2}月\d{1,2}"
    #     p = re.compile(regex_valid_time)
    #     if p.match(valid_time):
    #         return valid_time
    #     else:
    #         raise forms.ValidationError(u"证书有效日期格式错误", code="valid_time_invalid")


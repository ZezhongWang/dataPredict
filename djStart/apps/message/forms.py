# _*_ coding:utf-8 _*_
__author__ = 'w2w'
__date__ = '17-7-17 上午11:42'

from django import forms
from captcha.fields import CaptchaField


class LoginForms(forms.Form):
    account = forms.CharField(required=True)
    password = forms.CharField(required=True, min_length=5)


class RegisterForms(forms.Form):
    account = forms.CharField(required=True, min_length=5, max_length=20)
    password = forms.CharField(required=True, min_length=6, max_length=20)
    password2 = forms.CharField(required=True, min_length=6, max_length=20)
    captcha = CaptchaField(error_messages={"invalid": u"验证码错误"})
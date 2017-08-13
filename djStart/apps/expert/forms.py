# _*_ coding:utf-8 _*_
__author__ = 'w2w'
__date__ = '17-7-17 上午11:42'

from django import forms


class ExpertForm(forms.Form):
    expert_number = forms.CharField(required=True, min_length=8)
    valid_time = forms.CharField(required=True, max_length=10, min_length=10)


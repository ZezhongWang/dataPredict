# _*_ coding:utf-8 _*_
__author__ = 'w2w'
__date__ = '17-7-14 下午2:27'

import xadmin
from apps.expert.models import Expert


class ExpertAdmin(object):
    pass

xadmin.site.register(Expert, ExpertAdmin)

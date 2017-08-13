# _*_ coding:utf-8 _*_
__author__ = 'w2w'
__date__ = '17-7-14 下午8:02'

import xadmin

from apps.message.models import User
from xadmin import views


class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True


class GlobalSettings(object):
    site_title = "专家征集管理后台"
    site_footer = "专家征集系统"
    # menu_style = "accordion"


class UserAdmin(object):
    list_display = ['user_id', 'type']
    search_fields = ['user_id', 'type']
    list_filter = ['user_id', 'type']

xadmin.site.register(User, UserAdmin)
xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSettings)

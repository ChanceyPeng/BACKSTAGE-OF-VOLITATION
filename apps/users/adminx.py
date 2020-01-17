#!/usr/bin/env python
# encoding: utf-8

import xadmin
from xadmin import views
from .models import VerifyCode


class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True


class GlobalSettings(object):
    site_title = "千寻生鲜后台管理系统"
    site_footer = "2020 volitation.com All Rights Reserved"
    # menu_style = "accordion"


class VerifyCodeAdmin(object):
    list_display = ['code', 'mobile', "add_time"]
    search_fields = ['mobile']
    model_icon = 'fa fa-envelope'


xadmin.site.register(VerifyCode, VerifyCodeAdmin)
xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSettings)
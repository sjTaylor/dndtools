# -*- coding: utf-8 -*-

from django.urls import path
from dnd.rules.views import *

urlpatterns = (
    # 'dnd.rules.views',

    # rules list
    path(
        '',
        rule_list,
        name='rule_list',
    ),

    # rules
    path(
        '<rulebook_slug>--<rulebook_id>/<rule_slug>--<rule_id>/',
        rule_detail,
        name='rule_detail',
    ),

)

# -*- coding: utf-8 -*-

from django.conf.urls import url
from dnd.rules.views import *

urlpatterns = (
    # 'dnd.rules.views',

    # rules list
    url(
        r'^$',
        rule_list,
        name='rule_list',
    ),

    # rules
    url(
        r'^(?P<rulebook_slug>[^/]+)--(?P<rulebook_id>\d+)/(?P<rule_slug>[^/]+)--(?P<rule_id>\d+)/$',
        rule_detail,
        name='rule_detail',
    ),

)

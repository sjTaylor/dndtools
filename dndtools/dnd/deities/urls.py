# -*- coding: utf-8 -*-

from django.urls import path
from dnd.deities.views import *

urlpatterns = (
    # 'dnd.deities.views',

    # deities
    path(
        '',
        deity_list,
        name='deity_list',
    ),
    # deities > detail
    path(
        '<deity_slug>/',
        deity_detail,
        name='deity_detail',
    ),
)

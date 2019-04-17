# -*- coding: utf-8 -*-

from django.urls import path
from dnd.languages.views import *

urlpatterns = (
    # 'dnd.languages.views',

    # languages
    path(
        '',
        language_index,
        name='language_index'
    ),
    # languages > detail
    path(
        '<language_slug>/',
        language_detail,
        name='language_detail'
    ),
)

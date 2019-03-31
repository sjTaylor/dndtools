# -*- coding: utf-8 -*-

from django.conf.urls import url
from dnd.languages.views import *

urlpatterns = (
    # 'dnd.languages.views',

    # languages
    url(
        r'^$',
        language_index,
        name='language_index'
    ),
    # languages > detail
    url(
        r'^(?P<language_slug>[^/]+)/$',
        language_detail,
        name='language_detail'
    ),
)

# -*- coding: utf-8 -*-

from django.conf.urls import url
from dnd.contacts.views import *

urlpatterns = (
    # 'dnd.contacts.views',

    # contact
    url(
        r'^$',
        contact,
        name='contact',
    ),
    # contact > sent
    url(
        r'^sent/$',
        contact_sent,
        name='contact_sent',
    ),
    # staff
    url(
        r'^staff/$',
        staff,
        name='staff',
    ),
    # android
    url(
        r'^android/$',
        android,
        name='android',
    ),
)

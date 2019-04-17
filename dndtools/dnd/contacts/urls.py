# -*- coding: utf-8 -*-

from dnd.contacts.views import *
from django.urls import path

urlpatterns = (
    # 'dnd.contacts.views',

    # contact
    path(
        '',
        contact,
        name='contact',
    ),
    # contact > sent
    path(
        'sent/',
        contact_sent,
        name='contact_sent',
    ),
    # staff
    path(
        'staff/',
        staff,
        name='staff',
    ),
    # android
    path(
        'android/',
        android,
        name='android',
    ),
)

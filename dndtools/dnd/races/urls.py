# -*- coding: utf-8 -*-

from django.urls import path

from dnd.races.views import *

urlpatterns = (
    # 'dnd.races.views',

    # races
    path(
        '',
        race_index,
        name='race_index',
    ),
    # races > by rulebooks
    path(
        'by-rulebooks/',
        race_list_by_rulebook,
        name='race_list_by_rulebook',
    ),
    # races > rulebook
    path(
        '<rulebook_slug>--<rulebook_id>/',
        races_in_rulebook,
        name='races_in_rulebook',
    ),
    # races > rulebook > feat
    path(
        '<rulebook_slug>--<rulebook_id>/<race_slug>--<race_id>/',
        race_detail,
        name='race_detail',
    ),
    # racial types
    path(
        'types/',
        race_type_index,
        name='race_type_index'
    ),
    # race > detail
    path(
        'types/<race_type_slug>/',
        race_type_detail,
        name='race_type_detail'
    ),
)

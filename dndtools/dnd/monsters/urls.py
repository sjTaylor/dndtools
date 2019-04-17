# -*- coding: utf-8 -*-

from django.urls import path
from dnd.monsters.views import *


urlpatterns = (
    # 'dnd.monsters.views',

    # monsters
    path(
        '',
        monster_index,
        name='monster_index',
    ),
    # monsters > by rulebooks
    path(
        'by-rulebooks/',
        monster_list_by_rulebook,
        name='monster_list_by_rulebook',
    ),
    # monsters > rulebook
    path(
        '<rulebook_slug>--<rulebook_id>/',
        monsters_in_rulebook,
        name='monsters_in_rulebook',
    ),
    # monsters > rulebook > feat
    path(
        '<rulebook_slug>--<rulebook_id>/<monster_slug>--<monster_id>/',
        monster_detail,
        name='monster_detail',
    ),
)

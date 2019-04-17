# -*- coding: utf-8 -*-

from django.urls import path
from dnd.items.views import *


urlpatterns = (
    # 'dnd.items.views',

    # items
    path(
        '',
        item_index,
        name='item_index',
    ),
    # items > by rulebooks
    path(
        'by-rulebooks/',
        item_list_by_rulebook,
        name='item_list_by_rulebook',
    ),
    # items > rulebook
    path(
        '<rulebook_slug>--<rulebook_id>/',
        items_in_rulebook,
        name='items_in_rulebook',
    ),
    # items > rulebook > item
    path(
        '<rulebook_slug>--<rulebook_id>/<item_slug>--<item_id>/',
        item_detail,
        name='item_detail',
    ),
)

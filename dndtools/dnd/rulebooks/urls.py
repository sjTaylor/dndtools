# -*- coding: utf-8 -*-

from django.urls import path

from dnd.rulebooks.views import rulebook_list, edition_list, edition_detail, rulebook_detail

urlpatterns = [
    # 'dnd.rulebooks.views',

    # rulebooks
    path(
        '',
        rulebook_list,
        name='rulebook_list',
    ),
    # rulebooks > editions
    path(
        'editions/',
        edition_list,
        name='edition_list',
    ),
    # rulebooks > edition (lists books in an edition)
    path(
        '<edition_slug>--<edition_id>/',
        edition_detail,
        name='edition_detail',
    ),
    # rulebooks > edition > rulebook (rulebook detail, links to spells/feats)
    path(
        '<edition_slug>--<edition_id>/<rulebook_slug>--<rulebook_id>/',
        rulebook_detail,
        name='rulebook_detail',
    ),
]

# -*- coding: utf-8 -*-

from django.urls import path
import dnd.feats.views as views

urlpatterns = [
    # 'dnd.feats.views',

    # feats
    path(
        '',
        getattr(views, 'feat_index'),
        name='feat_index',
    ),
    # feats > categories
    path(
        'categories/',
        getattr(views, 'feat_category_list'),
        name='feat_category_list',
    ),
    # feats > categories > category
    path(
        'categories/<category_slug>/',
        getattr(views, 'feat_category_detail'),
        name='feat_category_detail',
    ),
    # feats > rulebook
    path(
        '<rulebook_slug>--<rulebook_id>/',
        getattr(views, 'feats_in_rulebook'),
        name='feats_in_rulebook',
    ),
    # feats > rulebook > feat
    path(
        '<rulebook_slug>--<rulebook_id>/<feat_slug>--<feat_id>/',
        getattr(views, 'feat_detail'),
        name='feat_detail',
    ),
]

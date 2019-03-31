# -*- coding: utf-8 -*-

from django.conf.urls import url
import dnd.feats.views as views

urlpatterns = [
    # 'dnd.feats.views',

    # feats
    url(
        r'^$',
        getattr(views, 'feat_index'),
        name='feat_index',
    ),
    # feats > categories
    url(
        r'^categories/$',
        getattr(views, 'feat_category_list'),
        name='feat_category_list',
    ),
    # feats > categories > category
    url(
        r'^categories/(?P<category_slug>[^/]+)/$',
        getattr(views, 'feat_category_detail'),
        name='feat_category_detail',
    ),
    # feats > rulebook
    url(
        r'^(?P<rulebook_slug>[^/]+)--(?P<rulebook_id>\d+)/$',
        getattr(views, 'feats_in_rulebook'),
        name='feats_in_rulebook',
    ),
    # feats > rulebook > feat
    url(
        r'^(?P<rulebook_slug>[^/]+)--(?P<rulebook_id>\d+)/(?P<feat_slug>[^/]+)--(?P<feat_id>\d+)/$',
        getattr(views, 'feat_detail'),
        name='feat_detail',
    ),
]

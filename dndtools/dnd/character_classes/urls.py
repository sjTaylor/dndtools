# -*- coding: utf-8 -*-

from django.conf.urls import url

import dnd.character_classes.views as views

urlpatterns = (
    # 'dnd.character_classes.views',

    # classes
    url(
        r'^$',
        getattr(views,'character_class_list'),
        name='character_class_list',
    ),
    # classes > detail
    url(
        r'^(?P<character_class_slug>[^/]+)/$',
        getattr(views,'character_class_detail'),
        name='character_class_detail',
    ),
    # classes > detail
    url(
        r'^(?P<rulebook_slug>[^/]+)--(?P<rulebook_id>\d+)/(?P<character_class_slug>[^/]+)/$',
        getattr(views,'character_class_detail'),
        name='character_class_variant_detail',
    ),
    # classes > detail > spells by level
    url(
        r'^(?P<character_class_slug>[^/]+)/spells-level-(?P<level>\d)/$',
        getattr(views,'character_class_spells'),
        name='character_class_spells',
    ),
    # classes > rulebook
    url(
        r'^rulebook/(?P<rulebook_slug>[^/]+)--(?P<rulebook_id>\d+)/$',
        getattr(views,'character_classes_in_rulebook'),
        name='character_classes_in_rulebook',
    ),
)

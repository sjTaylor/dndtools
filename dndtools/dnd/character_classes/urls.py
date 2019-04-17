# -*- coding: utf-8 -*-

from django.urls import path

import dnd.character_classes.views as views

urlpatterns = (
    # 'dnd.character_classes.views',

    # classes
    path(
        '',
        views.character_class_list,
        name='character_class_list',
    ),
    # classes > detail
    path(
        '<character_class_slug>/',
        getattr(views, 'character_class_detail'),
        name='character_class_detail',
    ),
    # classes > detail
    path(
        '<rulebook_slug>--<rulebook_id>/<character_class_slug>/',
        # '<character_class_slug>/',
        getattr(views, 'character_class_detail'),
        name='character_class_variant_detail',
    ),
    # classes > detail > spells by level
    path(
        '<character_class_slug>/spells-level-<level>/',
        getattr(views, 'character_class_spells'),
        name='character_class_spells',
    ),
    # classes > rulebook
    path(
        'rulebook/<rulebook_slug>--<rulebook_id>/',
        getattr(views, 'character_classes_in_rulebook'),
        name='character_classes_in_rulebook',
    ),
)

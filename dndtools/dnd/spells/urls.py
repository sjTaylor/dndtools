# -*- coding: utf-8 -*-

from django.urls import path
import dnd.spells.views as views


urlpatterns = (
    # 'dnd.spells.views',

    # spells
    path(
        '',
        views.spell_index,
        name='spell_index',
    ),
    # spells > rulebook
    path(
        '<rulebook_slug>--<rulebook_id>/',
        getattr(views, 'spells_in_rulebook'),
        name='spells_in_rulebook',
    ),
    # spells > rulebook > spell
    path(
        '<rulebook_slug>--<rulebook_id>/<spell_slug>--<spell_id>/',
        getattr(views, 'spell_detail'),
        name='spell_detail',
    ),
    # spells > descriptors
    path(
        'descriptors/',
        getattr(views, 'spell_descriptor_list'),
        name='spell_descriptor_list',
    ),
    # spells > descriptors > descriptor
    path(
        'descriptors/<spell_descriptor_slug>/',
        getattr(views, 'spell_descriptor_detail'),
        name='spell_descriptor_detail',
    ),
    # spells > schools
    path(
        'schools/',
        getattr(views, 'spell_school_list'),
        name='spell_school_list',
    ),
    # spells > schools > detail
    path(
        'schools/<spell_school_slug>/',
        getattr(views, 'spell_school_detail'),
        name='spell_school_detail',
    ),
    # spells > sub_schools > detail
    path(
        'sub-schools/<spell_sub_school_slug>/',
        getattr(views, 'spell_sub_school_detail'),
        name='spell_sub_school_detail',
    ),
    # spells > domains
    path(
        'domains/',
        getattr(views, 'spell_domain_list'),
        name='spell_domain_list',
    ),
    # spells > domains > detail
    path(
        'domains/<spell_domain_slug>/',
        getattr(views, 'spell_domain_detail'),
        name='spell_domain_detail',
    ),

    # spells > domains > detail (variant)
    path(
        'domains/<rulebook_slug>--<rulebook_id>/<spell_domain_slug>/',
        getattr(views, 'spell_domain_detail'),
        name='spell_variant_domain_detail',
    ),

    path(
        'verify/spell/<spell_id>/',
        getattr(views, 'spell_verify'),
        name='spell_verify',
    ),
)

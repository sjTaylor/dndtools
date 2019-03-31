# -*- coding: utf-8 -*-

from django.conf.urls import url
import dnd.spells.views as views


urlpatterns = (
    # 'dnd.spells.views',

    # spells
    url(
        r'^$',
        getattr(views, 'spell_index'),
        name='spell_index',
    ),
    # spells > rulebook
    url(
        r'^(?P<rulebook_slug>[^/]+)--(?P<rulebook_id>\d+)/$',
        getattr(views, 'spells_in_rulebook'),
        name='spells_in_rulebook',
    ),
    # spells > rulebook > spell
    url(
        r'^(?P<rulebook_slug>[^/]+)--(?P<rulebook_id>\d+)/(?P<spell_slug>[^/]+)--(?P<spell_id>\d+)/$',
        getattr(views, 'spell_detail'),
        name='spell_detail',
    ),
    # spells > descriptors
    url(
        r'^descriptors/$',
        getattr(views, 'spell_descriptor_list'),
        name='spell_descriptor_list',
    ),
    # spells > descriptors > descriptor
    url(
        r'^descriptors/(?P<spell_descriptor_slug>[^/]+)/$',
        getattr(views, 'spell_descriptor_detail'),
        name='spell_descriptor_detail',
    ),
    # spells > schools
    url(
        r'^schools/$',
        getattr(views, 'spell_school_list'),
        name='spell_school_list',
    ),
    # spells > schools > detail
    url(
        r'^schools/(?P<spell_school_slug>[^/]+)/$',
        getattr(views, 'spell_school_detail'),
        name='spell_school_detail',
    ),
    # spells > sub_schools > detail
    url(
        r'^sub-schools/(?P<spell_sub_school_slug>[^/]+)/$',
        getattr(views, 'spell_sub_school_detail'),
        name='spell_sub_school_detail',
    ),
    # spells > domains
    url(
        r'^domains/$',
        getattr(views, 'spell_domain_list'),
        name='spell_domain_list',
    ),
    # spells > domains > detail
    url(
        r'^domains/(?P<spell_domain_slug>[^/]+)/$',
        getattr(views, 'spell_domain_detail'),
        name='spell_domain_detail',
    ),

    # spells > domains > detail (variant)
    url(
        r'^domains/(?P<rulebook_slug>[^/]+)--(?P<rulebook_id>\d+)/(?P<spell_domain_slug>[^/]+)/$',
        getattr(views, 'spell_domain_detail'),
        name='spell_variant_domain_detail',
    ),

    url(
        r'^verify/spell/(?P<spell_id>\d+)/$',
        getattr(views, 'spell_verify'),
        name='spell_verify',
    ),
)

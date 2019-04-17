# -*- coding: utf-8 -*-

from django.urls import path

from dnd.skills.views import skill_list, skill_detail, skills_in_rulebook

urlpatterns = (
    # 'dnd.skills.views',

    # skills
    path(
        '',
        skill_list,
        name='skill_list',
    ),
    # skills > detail
    path(
        '<skill_slug>/',
        skill_detail,
        name='skill_detail',
    ),
    # skills > detail (variant)
    path(
        '<rulebook_slug>--<rulebook_id>/<skill_slug>/',
        skill_detail,
        name='skill_variant_detail',
    ),
    # skills > rulebook
    path(
        'rulebook/<rulebook_slug>--<rulebook_id>/',
        skills_in_rulebook,
        name='skills_in_rulebook',
    ),
)

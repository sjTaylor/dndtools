# -*- coding: utf-8 -*-

from django.conf.urls import include, url
from django.urls import path
from django.views.generic import TemplateView, RedirectView
from django.conf.urls.static import static
from django.contrib.sitemaps.views import sitemap
from .feeds import AdminLogFeed
from .sitemap import sitemaps
from .views import index
from dndproject import settings
# from .rulebooks.urls import urlpatterns as featpatterns

from dnd.views import inaccurate_content, inaccurate_content_sent, very_secret_url

# prefix = 'dnd.views'

urlpatterns = [

    # index
    url(
        r'^$',
        index,
        name='index',
    ),


    # Rulebooks
    path('rulebooks/', include('dnd.rulebooks.urls')),

    # Feats
    path('feats/', include('dnd.feats.urls')),

    # Spells
    path('spells/', include('dnd.spells.urls')),

    # Classes
    path('classes/', include('dnd.character_classes.urls')),

    # Skills
    path('skills/', include('dnd.skills.urls')),

    # Races
    path('races/', include('dnd.races.urls')),

    # Monsters
    path('monsters/', include('dnd.monsters.urls')),

    # Items
    path('items/', include('dnd.items.urls')),

    # Languages
    path('languages/', include('dnd.languages.urls')),

    # Contacts
    path('contacts/', include('dnd.contacts.urls')),

    # Rules
    path('rules/', include('dnd.rules.urls')),

    # deities
    path('deities/', include('dnd.deities.urls')),

    # OTHERS

    url(r'^robots\.txt$', TemplateView.as_view(template_name='robots.txt', content_type='text/plain')),

    # inaccurate
    url(
        r'^inaccurate_content/$',
        inaccurate_content,
        name='inaccurate_content',
    ),
    # inaccurate > sent
    url(
        r'^inaccurate_content/sent/$',
        inaccurate_content_sent,
        name='inaccurate_content_sent',
    ),
    url(r'^rss.xml$', AdminLogFeed()),
    url(r'^sitemap\.xml$', sitemap, {'sitemaps': sitemaps}),

    # job
    url(
        r'^very_secret_url/$',
        very_secret_url,
        name='very_secret_url',
    ),

    # # MOBILE
    # url(r'^m/', include('dnd.mobile.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += [
    url('^contact/$', RedirectView.as_view(url='/contacts/')),
    url('^staff/$', RedirectView.as_view(url='/contacts/staff/')),
    url('^editions/$', RedirectView.as_view(url='/rulebooks/editions/')),
    url('^feat-(?P<feat_id>\d+)-(.*)\.html$', RedirectView.as_view(url='/feats/a--1/a--%(feat_id)s/')),
]

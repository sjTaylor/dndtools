from django.conf.urls import include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = [

    # url(r'^admin/', include(admin.site.urls)),
    # TODO
    # (r'^sitemap\.xml$', 'django.contrib.sitemaps.views.sitemap', {'sitemaps': sitemaps}),
    url(r'^', include('dnd.urls')),
]

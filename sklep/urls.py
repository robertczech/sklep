from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'produkt.views.index'),
    # url(r'^sklep/', include('sklep.foo.urls')),
    url(r'^kategoria/(?P<kategoria>.*)/$', 'produkt.views.kategoria'),
    url(r'^produkt/(?P<produkt>.*)/$', 'produkt.views.produkt'),
    # url(r'^sklep/', include('sklep.foo.urls')),
    
    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    (r'^photos/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': '/home/rob/sklep/photos/'}),
)

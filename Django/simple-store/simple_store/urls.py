from django.conf.urls import patterns, include, url
from store import urls as appurls
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'simple_store.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^', include(appurls)),
    url(r'^admin/', include(admin.site.urls)),
)

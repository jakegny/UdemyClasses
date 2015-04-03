from django.conf.urls import patterns, include, url
import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'image_share.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', views.upload, name = "main"),
    url(r'^handl/$', views.hnd_load, name = "handl"),
)

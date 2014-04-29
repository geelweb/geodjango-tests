from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^$', 'shops.views.home', name='home'),
)

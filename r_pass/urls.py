from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    # Examples:
    url(r'^service/.*/(?P<service_id>[0-9]+)/edit/?$', 'r_pass.views.edit'),
    url(r'^service/.*/(?P<service_id>[0-9]+)/?$', 'r_pass.views.service'),
    url(r'^create/?$', 'r_pass.views.create'),
    url(r'', 'r_pass.views.home'),
)

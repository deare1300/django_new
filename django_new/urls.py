from django.conf.urls import patterns, include, url

from django.contrib import admin

import test_dj
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'django_new.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^test_dj/',include('test_dj.urls',namespace='test_dj')),
)

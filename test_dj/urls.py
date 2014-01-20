'''
Created on Jan 17, 2014

@author: root
'''
from test_dj.views import atomic
from django.conf.urls import patterns,url  
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'django_new.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', atomic),
    url(r'^atomic$/',atomic),
    
)
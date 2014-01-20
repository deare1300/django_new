'''
Created on Jan 17, 2014

@author: root
'''
from test_dj.views import atomic
from django.conf.urls import patterns,url
from test_dj import views   
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'django_new.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', views.IndexView.as_view()),
    url(r'^atomic/$',atomic),
    
    url('^index/$',views.index,name='index')
    
)
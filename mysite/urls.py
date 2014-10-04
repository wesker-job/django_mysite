from django.conf.urls import patterns, include, url
from mysite.views import *
from restaurants.views import *
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    #url(r'^admin/', include(admin.site.urls)),
    url(r'comment/(\d{1,2})/$', 'restaurants.views.comment'),
    url(r'rest_list/$', 'restaurants.views.rest_list'),
    url(r'menu1/$', 'restaurants.views.menu1'),
    #url(r'menu1/(\d{1,5})/$', 'restaurants.views.menu1'),
    url(r'welcome/$', 'mysite.views.welcome'),
    url(r'^menu/$', 'restaurants.views.menu'),
    url(r'^menu_test/$', 'mysite.views.menu'),
    url(r'^here/$', 'mysite.views.here'),
    url(r'^(\d{1,2})/plus/(\d{1,2})/$', 'mysite.views.math'),
)

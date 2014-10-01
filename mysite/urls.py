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
    url(r'^menu/', 'restaurants.views.menu'),
    url(r'^menu1/$', 'mysite.views.menu'),
    url(r'^here/$', 'mysite.views.here'),
    url(r'^(\d{1,2})/plus/(\d{1,2})/$', 'mysite.views.math'),
)

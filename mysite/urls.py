from django.conf.urls import patterns, include, url
from mysite.views import *
from books import views
from contact.views import contact, thanks
from django.contrib import admin
admin.autodiscover()

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
	url(r'^hello/$', hello), 
	url(r'^time/$', current_datetime),
	#url(r'^time/plus/1/$', one_hour_ahead),
	#url(r'^time/plus/2/$', two_hours_ahead),
	#url(r'^time/plus/3/$', three_hours_ahead),
	#url(r'^time/plus/4/$', four_hours_ahead),
	url(r'^time/plus/(\d{1,2})/$', hours_ahead),
	url(r'^search/$', views.search),
	url(r'^contact/$', contact),
	url(r'^thanks/$', thanks),
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^mysite/', include('mysite.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/$', include(admin.site.urls)),
)

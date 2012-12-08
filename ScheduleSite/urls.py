from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

#from IrishSchedule import views


urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^IrishSchedule/', include('IrishSchedule.urls')),
    # Examples:
    # url(r'^$', 'ScheduleSite.views.home', name='home'),
    # url(r'^ScheduleSite/', include('ScheduleSite.foo.urls')),


    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:

)

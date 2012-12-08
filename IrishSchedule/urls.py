from django.conf.urls import patterns, url
#from django.models import IrishSchedule
from IrishSchedule import views
#from IrishSchedule.views import courses

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^(?P<deptkey>[A-Z]*)/$', views.courses, name='courses'),
    url(r'^(?P<course_no>\w*)/$', views.sections, name='sections'),)
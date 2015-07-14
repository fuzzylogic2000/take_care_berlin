from django.conf.urls import patterns, include, url
from . import views

urlpatterns = patterns('',
    url(r'^$', views.kita_list),
    url(r'^kita/(?P<pk>[0-9]+)/$', views.kita_detail),
)
from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include
from artlink import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^activity/(?P<activity_slug>[\w\-]+)/$', views.show_activity, name='show_activity'),
    url(r'^add$', views.submit_activity, name='add'),
    url(r'^browse$', views.browse, name='browse'),
    url(r'^about$', views.about, name='about'),
    url(r'^index$', views.index, name='index'),
]

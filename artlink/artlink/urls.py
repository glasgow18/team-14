from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include
from artlink import views

urlpatterns = [
	url(r'^admin/', admin.site.urls),
    url(r'^$', views.index, name='index'),
    url(r'^activity/(?P<activity_slug>[\w\-]+)/$', views.activity_show, name='activity_show'),
    url(r'^$', views.add, name='add'),
    url(r'^$', views.browse, name='browse'),
    url(r'^$', views.about, name='about'),
]

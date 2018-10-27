from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include
from artlink import views

urlpatterns = [
	url(r'^admin/', admin.site.urls),
    url(r'^$', views.index, name='index'),
    url(r'^activity/(?P<activity_slug>[\w\-]+)/$', views.activity_show, name='activity_show'),
    url(r'^add$', views.add, name='add'),
    url(r'^browse$', views.browse, name='browse'),
    url(r'^about$', views.about, name='about'),

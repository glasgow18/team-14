from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include
from artlink import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^activity/(?P<activity_slug>[\w\-]+)/$', views.show_place, name='show_place'),
    url(r'^$', views.add, name='add'),
    url(r'^$', views.browse, name='browse'),
    url(r'^$', views.about, name='about'),
    url(r'^admin/', admin.site.urls),
]

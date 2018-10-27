from django.conf.urls import include, url
from django.contrib import admin
from artlink import views

urlpatterns = (
    # Examples:
    # url(r'^$', 'artlink.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.index, name='index'),
    url(r'^artlink/', include('artlink.urls')),
)

from django.conf.urls import include, url
from django.contrib import admin
from artlink import views

urlpatterns = (
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.index, name='index'),
    # link to main app urls...
    url(r'^artlink/', include('artlink.urls')),
)

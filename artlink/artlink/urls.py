from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include
from artlink import views

#TODO links will have format site/artlink/url... consider moving everything to site/url

urlpatterns = [
    # index view
    url(r'^$', views.index, name='index'),
    # slugify the activity title
    url(r'^activity/(?P<activity_slug>[\w\-]+)/$', views.show_activity, name='show_activity'),
    # add an activity view
    url(r'^add$', views.submit_activity, name='add'),
    # browse activities view
    url(r'^browse$', views.browse, name='browse'),
    # about Artlink :-)
    url(r'^about$', views.about, name='about'),
    # import
    url(r'^faq$', views.faq, name='faq'),
]

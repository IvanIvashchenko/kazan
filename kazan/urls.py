from django.conf.urls import patterns, url

from kazan import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    # ex: /kazan/user/8
    url(r'^user/(?P<user_id>\d+)/$', views.user_detail, name='user_detail'),
    # ex: /kazan/ad/4
    url(r'^ad/(?P<ad_id>\d+)/$', views.ad_detail, name='ad_detail'),
)
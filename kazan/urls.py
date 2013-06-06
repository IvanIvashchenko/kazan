from django.conf.urls import patterns, url

from kazan import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    # ex: /kazan/user/8
    url(r'^user/(?P<user_id>\d+)/$', views.user_detail, name='user'),
    # ex: /kazan/ad/4
    url(r'^ad/(?P<ad_id>\d+)/$', views.ad_detail, name='ad_detail'),
    url(r'^ad/$', views.create_ad, name='create_ad'),
    url(r'^sale/(?P<sale_id>\d+)/$', views.sale_detail, name='sale_detail'),
    url(r'^buy/(?P<ad_id>\d+)/$', views.buy_ad, name='buy_ad'),
    url(r'^registration/register/$', views.owner_registration, name='registration'),
    url(r'^registration/login/$', views.login_request, name='login'),
    url(r'^registration/logout/$', views.logout_request, name='logout'),
)

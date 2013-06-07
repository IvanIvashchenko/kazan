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
    url(r'^registration/login/$', views.login_request, name='login'),
    url(r'^registration/logout/$', views.logout_request, name='logout'),

    url(r'^registration/user/password/reset/$', views.password_reset_custom, name="password_reset"),

    url(r'^registration/user/password/reset/done/$', 'django.contrib.auth.views.password_reset_done',
        {'template_name': 'registration/pass_reset_done.html'}),
    url(r'^registration/user/password/reset/(?P<uidb36>[0-9A-Za-z]+)-(?P<token>.+)/$', 'django.contrib.auth.views.password_reset_confirm',
        {'post_reset_redirect': '/kazan/registration/user/password/done/', 'template_name': 'registration/pass_reset_confirm.html'}),
    url(r'^registration/user/password/done/$', 'django.contrib.auth.views.password_reset_complete',
        {'template_name': 'registration/pass_reset_complete.html'}),
)

from django.conf.urls import patterns, url
from registration.forms import RegistrationFormUniqueEmail

from kazan import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    # ex: /kazan/user/8
    url(r'^userprofile/(?P<user_id>\d+)/$', views.user_detail, name='user_detail'),
    # ex: /kazan/ad/4
    url(r'^ad/(?P<ad_id>\d+)/$', views.ad_detail, name='ad_detail'),
    url(r'^sale/(?P<sale_id>\d+)/$', views.sale_detail, name='sale_detail'),
    # url(r'^register/$', 'registration.views.register', {'form': RegistrationFormUniqueEmail}, name='registration_register'),
)
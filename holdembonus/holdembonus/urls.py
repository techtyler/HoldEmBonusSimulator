from django.conf.urls import patterns, include, url
from django.contrib.auth.models import User
from django.contrib import admin
from rest_framework import routers







urlpatterns = patterns(
	'',
	url(r'^auth/', 'holdembonus.views.auth_view'),
	url(r'^rest-auth/', include('rest_auth.urls')),
	url(r'^rest-auth/registration/', include('rest_auth.registration.urls')),
	url(r'^home', 'holdembonus.views.home', name='home'),
	url(r'^$', 'holdembonus.views.index', name='index'),

	
	

    #url(r'^views/index.html/$', 'holdembonus.views.index'),
    #url(r'^views/(?P<page>[-\w]+.html)/$', 'holdembonus.views.angular_views'),
    #url(r'^(?P<path>.*)/$', 'holdembonus.views.angular_redirector'),
)



# urlpatterns = patterns(
#     '',
#     # Examples:
#     url(r'^', include(router.urls)),
#     # url(r'^blog/', include('blog.urls')),
# #     
#     url(r'^admin/', include(admin.site.urls)),
#     #url(r'^cards/', include('cards.urls')),
#     url(r'^foundation/', include('foundation.urls')),
#     url(r'^test/', include('rest_framework.urls', namespace='rest_framework')),
#     url('^.*$', IndexView.as_view(), name='index'), #This url makes sure to pass anything that doesnt match to the angular service
# )


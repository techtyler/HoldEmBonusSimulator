from django.conf.urls import patterns, include, url
from django.contrib.auth.models import User
from django.contrib import admin
from rest_framework import routers
#from players.views import PlayerAccountViewSet
#from views import IndexView



# Routers provide an easy way of automatically determining the URL conf.
#router = routers.SimpleRouter()
#router.register(r'players', PlayerAccountViewSet)


urlpatterns = patterns('',
	url(r'^foundation/', include('foundation.urls')),
    url(r'^$', 'holdembonus.views.index', name='index'),

    #url(r'^views/index.html/$', 'holdembonus.views.index'),
    url(r'^views/(?P<page>[-\w]+.html)/$', 'myproject.views.angular_views'),
    url(r'^(?P<path>.*)/$', 'holdembonus.views.angular_redirector'),
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


from django.conf.urls import patterns, url
from cards import views

urlpatterns = patterns('',
    url(r'^(?P<card_id>..)/$', views.card, name='card'),
)
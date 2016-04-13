#coding: utf-8
from django.conf.urls import url
from helloDjango.subscriptions.views import success, subscribe
urlpatterns = [
    url(r'^$', subscribe, name='subscribe'),
    url(r'^(\d+)/$', success, name="success"),
]

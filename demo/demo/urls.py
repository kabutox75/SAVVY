# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf.urls import url

from .views import CategoryEncodingView, ScalarEncodingView, DateEncodingView

urlpatterns = [
    url(r'^$', CategoryEncodingView.as_view(), name='categoryencoding'),

	url(r'^categoryencoding$', CategoryEncodingView.as_view(), name='categoryencoding'),
	url(r'^scalarencoding$', ScalarEncodingView.as_view(), name='scalarencoding'),
	url(r'^dateencoding$', DateEncodingView.as_view(), name='dateencoding'),
]

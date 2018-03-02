# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.core.files.storage import default_storage

from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models.fields.files import FieldFile
from django.views.generic import FormView
from django.views.generic.base import TemplateView
from django.contrib import messages

from .forms import ContactForm, FilesForm, ContactFormSet


class CategoryEncodingView(TemplateView):
    template_name = 'demo/categoryencoding.html'
	
class ScalarEncodingView(TemplateView):
    template_name = 'demo/scalarencoding.html'
	
class DateEncodingView(TemplateView):
    template_name = 'demo/dateencoding.html'

from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from django.template import Template, Context
from django.template.loader import get_template, render_to_string
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.db.models import Count
from django.core import serializers
from django.contrib.staticfiles.storage import staticfiles_storage
from django.utils.http import urlencode


# Create your views here.

@login_required
def index(request):
    return render(request, 'django_bcf_manager/index.html', {})
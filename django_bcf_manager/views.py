from django.shortcuts import render, redirect
# from django.http import HttpResponse, Http404
# from django.template import Template, Context
# from django.template.loader import get_template, render_to_string
# from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
# from django.db.models import Count
# from django.core import serializers
# from django.contrib.staticfiles.storage import staticfiles_storage
# from django.utils.http import urlencode
from django_bcf_manager.forms import *


from .models import *
# Create your views here.

@login_required
def index(request):
    return render(request, 'django_bcf_manager/index.html', {})


@login_required
def topics(request):
    topics = Topic.objects.all().order_by('-dt_modification')
    return render(request, 'django_bcf_manager/topics.html', {'topics': topics})


@login_required
def bcffile_add(request):
    c = {}
    if request.method == 'POST':
        form = BCFFileForm(request.POST, request.FILES)
        if form.is_valid():
            bcffileobj = BcfFile() # new object
            bcffileobj.handlePostRequest(request)
            return redirect('ifc_summary',ifc_id=bcffileobj.id)
    else:
        c['form'] = BcfFile()
    return render(request, 'django_bcf_manager/addfile.html',c)
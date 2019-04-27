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

from rest_framework import viewsets
from .serializers import TopicSerializer


from .models import *
# Create your views here.

@login_required
def index(request):
    return render(request, 'django_bcf_manager/index.html', {})


@login_required
def topics(request):
    # POST means a new file
    if request.method == 'POST':
        form = BCFFileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('topics')
    else:
        form = BCFFileForm()
    topics = Topic.objects.all().order_by('-creation_date')
    return render(request, 'django_bcf_manager/topics.html', {'topics': topics, 'form': form})


# API views
class TopicViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Topic.objects.all().order_by('-creation_date')
    serializer_class = TopicSerializer
from django.urls import include, path, re_path
from django.contrib import admin


from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('topics', views.topics, name='topics'),
]
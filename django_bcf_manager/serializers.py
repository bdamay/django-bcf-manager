from django.contrib.auth.models import User, Group
from .models import Topic
from rest_framework import serializers


class TopicSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Topic
        fields = ['guid', 'topic_type', 'title']

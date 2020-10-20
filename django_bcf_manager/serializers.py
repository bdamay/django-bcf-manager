from django.contrib.auth.models import User, Group
from .models import Topic
from rest_framework import serializers


class TopicSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Topic
        fields = ['guid', 'title', 'creation_author', 'modified_author', 'assigned_to', 'stage',
                  'topic_status', 'topic_type', 'creation_date', 'modified_date', 'labels']

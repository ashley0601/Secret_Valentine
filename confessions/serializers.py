# confessions/serializers.py
from rest_framework import serializers
from .models import Confession, Feedback

class ConfessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Confession
        fields = ['id', 'text', 'latitude', 'longitude', 'location_name', 'color', 'likes', 'created_at']
        read_only_fields = ['id', 'likes', 'created_at']

class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = ['id', 'text', 'created_at']
        read_only_fields = ['id', 'created_at']
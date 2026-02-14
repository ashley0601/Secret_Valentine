from django.db import models
# confessions/models.py
import uuid
from django.db import models

class Confession(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    text = models.TextField()
    latitude = models.FloatField()
    longitude = models.FloatField()
    location_name = models.CharField(max_length=255)
    color = models.CharField(max_length=7, default='#ff4d6d')
    likes = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.location_name}: {self.text[:50]}..."
    
    def to_dict(self):
        return {
            'id': str(self.id),
            'text': self.text,
            'location': {
                'lat': self.latitude,
                'lng': self.longitude,
                'name': self.location_name
            },
            'color': self.color,
            'likes': self.likes,
            'timestamp': int(self.created_at.timestamp() * 1000)
        }

class Feedback(models.Model):
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Feedback: {self.text[:50]}..."
# Create your models here.

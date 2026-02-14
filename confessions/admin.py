# confessions/admin.py
from django.contrib import admin
from .models import Confession, Feedback

@admin.register(Confession)
class ConfessionAdmin(admin.ModelAdmin):
    list_display = ['location_name', 'text_preview', 'likes', 'created_at']
    list_filter = ['created_at', 'color']
    search_fields = ['text', 'location_name']
    readonly_fields = ['created_at']
    
    def text_preview(self, obj):
        return obj.text[:100] + '...' if len(obj.text) > 100 else obj.text

@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ['text_preview', 'created_at']
    readonly_fields = ['created_at']
    
    def text_preview(self, obj):
        return obj.text[:100] + '...' if len(obj.text) > 100 else obj.text
# Register your models here.

from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django.db.models import F
from .models import Confession, Feedback
from .serializers import ConfessionSerializer, FeedbackSerializer

def index(request):
    """Render the main SPA template"""
    return render(request, 'confessions/index.html')

class ConfessionViewSet(viewsets.ModelViewSet):
    queryset = Confession.objects.all()
    serializer_class = ConfessionSerializer
    
    def get_queryset(self):
        queryset = Confession.objects.all()
        search = self.request.query_params.get('search', None)
        if search:
            queryset = queryset.filter(
                models.Q(text__icontains=search) | 
                models.Q(location_name__icontains=search)
            )
        return queryset
    
    @action(detail=True, methods=['post'])
    def like(self, request, pk=None):
        confession = self.get_object()
        confession.likes = F('likes') + 1
        confession.save()
        confession.refresh_from_db()
        return Response({'likes': confession.likes})

class FeedbackViewSet(viewsets.ModelViewSet):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer
# Create your views here.

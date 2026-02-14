# confessions/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'confessions', views.ConfessionViewSet)
router.register(r'feedback', views.FeedbackViewSet)

urlpatterns = [
    path('', views.index, name='index'),
    path('api/', include(router.urls)),
]
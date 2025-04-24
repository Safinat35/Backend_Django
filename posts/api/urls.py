from django.urls import path
from .views import PostViewSet
from rest_framework.routers import DefaultRouter
from django.urls import path
from posts.views import classify_text

urlpatterns = [
    path('classify/', classify_text),
]
post_router = DefaultRouter()
post_router.register(r'posts', PostViewSet)
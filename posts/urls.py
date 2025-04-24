# posts/urls.py by chatgpt

from django.urls import path
from .views import classify_text  # or whatever your view is called

urlpatterns = [
    path('predict/', classify_text),
]

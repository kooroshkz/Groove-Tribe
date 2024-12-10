from django.urls import path
from .views import index, CreateSession, JoinSession

urlpatterns = [
    path('', index, name='index'),
    path('create/', CreateSession.as_view(), name='create-session'),
    path('join/<str:session_id>/', JoinSession.as_view(), name='join-session'),
    path('join/', JoinSession.as_view(), name='join-session-query'),  # New URL pattern for query params
]

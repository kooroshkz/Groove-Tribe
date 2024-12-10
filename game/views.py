from django.shortcuts import render, redirect
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Session, Song
from .serializers import SessionSerializer

def index(request):
    return render(request, 'game/index.html')

class CreateSession(APIView):
    def post(self, request):
        nickname = request.POST.get('nickname')  # Get the nickname
        # Generate a random 6-digit session code
        import random
        session_id = ''.join(random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890', k=6))
        session = Session.objects.create(session_id=session_id, host=nickname)
        return redirect(f'/join/{session_id}/?nickname={nickname}')

class JoinSession(APIView):
    def get(self, request, session_id=None):
        if not session_id:  # If session_id is not in the path, look for a query parameter
            session_id = request.GET.get('session_id')
        nickname = request.GET.get('nickname')
        try:
            session = Session.objects.get(session_id=session_id)
            return render(request, 'game/session.html', {
                'session_id': session_id,
                'nickname': nickname
            })
        except Session.DoesNotExist:
            return Response({"error": "Session not found"}, status=status.HTTP_404_NOT_FOUND)

from django.db import models

class Session(models.Model):
    session_id = models.CharField(max_length=6, unique=True)
    host = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

class Song(models.Model):
    session = models.ForeignKey(Session, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)
    preview_url = models.URLField()

class Reaction(models.Model):
    session = models.ForeignKey(Session, on_delete=models.CASCADE)
    user = models.CharField(max_length=100)
    meme_url = models.URLField()

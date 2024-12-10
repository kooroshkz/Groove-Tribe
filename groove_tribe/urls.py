from django.contrib import admin
from django.urls import path, include  # Import include for including app URLs

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("game.urls")),  # Include game app's URLs
]

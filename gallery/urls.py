from django.contrib import admin
from django.urls import path
from .views import GalleryView


urlpatterns = [
    # Implementing logic with class-based way
    path('load_image', GalleryView.as_view())
]

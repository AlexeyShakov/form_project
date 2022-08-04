from django.contrib import admin
from django.urls import path
from .views import GalleryView, ListGallery
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    # Implementing logic with class-based way
    path('load_image', GalleryView.as_view()),
    path('list_image', ListGallery.as_view()),
# It's needed to get the access to media files
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

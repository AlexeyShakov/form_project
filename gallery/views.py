from django.shortcuts import render
from django.views import View
from .forms import GalleryUploadForm
from django.http import HttpResponseRedirect
from .models import Gallery
from django.views.generic.edit import CreateView


class GalleryView(CreateView):
    model = Gallery
    fields = "__all__"
    template_name = "gallery/load_file.html"
    success_url = "load_image"

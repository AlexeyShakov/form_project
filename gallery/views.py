from .models import Gallery
from django.views.generic.edit import CreateView
from django.views.generic import ListView

class ListGallery(ListView):
    model = Gallery
    template_name ="gallery/list_file.html"
    # Change the name of parameter going to .html
    context_object_name = "records"

class GalleryView(CreateView):
    model = Gallery
    fields = "__all__"
    template_name = "gallery/load_file.html"
    success_url = "load_image"

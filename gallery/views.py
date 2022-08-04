from django.shortcuts import render
from django.views import View
from .forms import GalleryUploadForm
from django.http import HttpResponseRedirect

# This func is needed to get the data(some file) and store it in another file
# We use .chunks() in order to decrease the load from our RAM
def storage_file(file):
    name = file.name
    with open(f'gallery_tmp/{name}', 'wb+') as new_file:
        for chunk in file.chunks():
            new_file.write(chunk)


# Create your views here.
class GalleryView(View):
    def get(self, request):
        form = GalleryUploadForm()
        # the parameter 'context' serves for sending the data to .html file
        return render(request, "gallery/load_file.html", context={'form': form})

    def post(self, request):
        # Filling the form with data
        form = GalleryUploadForm(request.POST, request.FILES)
        if form.is_valid():
            # Saves a file
            storage_file(request.FILES['image'])
            return HttpResponseRedirect("load_image")
        return render(request, "gallery/load_file.html", context={'form': form})
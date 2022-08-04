from django.shortcuts import render
from django.views import View
from .forms import GalleryUploadForm
from django.http import HttpResponseRedirect
from .models import Gallery



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
            # Creating an instance and save it with the model
            new_image = Gallery(image=request.FILES['image'])
            new_image.save()
            return HttpResponseRedirect("load_image")
        return render(request, "gallery/load_file.html", context={'form': form})
from django.shortcuts import render
from django.views import View

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
        return render(request, "gallery/load_file.html")

    def post(self, request):
        storage_file(request.FILES['image'])
        return render(request, "gallery/load_file.html")
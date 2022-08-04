from django.db import models

# Create your models here.


class Gallery(models.Model):
    # We store only link to the file not the exact file!!! We point where we store a file in 'upload_to' parameter
    image = models.FileField(upload_to='my_data')
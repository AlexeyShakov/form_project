from django.db import models
from django.core.validators import MinLengthValidator

# Create your models here.

class Feedback(models.Model):
    name = models.CharField(max_length=15, validators=[MinLengthValidator(3)])
    last_name = models.CharField(max_length=15)
    feedback = models.TextField()
    rating = models.PositiveSmallIntegerField()

    def __str__(self):
        return f"{self.name} - {self.last_name} - {self.feedback} - {self.rating}"
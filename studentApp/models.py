from django.db import models
from django.utils import timezone

# Create your models here.
class Student(models.Model):

    name = models.CharField("Student Name",max_length=100)
    email = models.EmailField("Email Address",max_length=255, null=True, blank=True)
    dob = models.DateField("Birth Date", default=timezone.now, blank=True,help_text="Format:yyyy-mm-dd")

    def __str__(self):
        return self.name



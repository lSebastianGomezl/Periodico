from datetime import datetime
from distutils.command.upload import upload

from time import timezone
from django.db import models

# Create your models here.



class Notice(models.Model):
    id_notice = models.BigAutoField(primary_key=True)
    first_name = models.CharField(max_length=50)
    type_notice = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
    imagen = models.ImageField(upload_to="images", null=True)
    def __str__(self):
        return self.description
from pyexpat import model
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class contact(models.Model):
    n = models.TextField()
    msg = models.TextField()


    def __str__(self):
        return self.n


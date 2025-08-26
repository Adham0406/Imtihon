from email.charset import Charset

from django.db import models

class Notebook(models.Model):
    model= models.CharField(max_length=120)
    color=models.CharField(max_length=120)
    photo=models.ImageField(upload_to='photo', blank=True,null=True)
    price=models.DecimalField(max_digits=10,decimal_places=2)

def __str__(self):
    return self.model

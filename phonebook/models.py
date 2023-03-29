from django.db import models

# Create your models here.


class Vcard(models.Model):
    name = models.CharField(max_length=200)
    contact = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
    
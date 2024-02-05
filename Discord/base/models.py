from django.db import models

# Create your models here.

class Room(models.Model):
    #host = 
    #topic = 
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True) #Może powstać bez opisu
    #participants =
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True) #zapisuje tylko pierwsze stworzenie

    def __str__(self):
        return self.name
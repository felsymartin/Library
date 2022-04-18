from django.db import models

# Create your models here.

class books(models.Model):
    name = models.CharField(max_length = 100)
    author = models.CharField(max_length = 30)
    language = models.CharField(max_length = 30)    
    genre = models.CharField(max_length=50)
    image = models.ImageField(upload_to = 'pics')    
    description = models.TextField()
    charge = models.IntegerField()    
    date = models.DateTimeField(auto_now_add = True)
    offer = models.BooleanField(default = False)


from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=512)
    price = models.IntegerField()
    description = models.TextField()
   
    def __str__(self):
        return str(self.name)

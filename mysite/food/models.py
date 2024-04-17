from django.db import models

# Create your models here.
class Food(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.CharField(max_length=600, default='https://www.foodista.com/sites/default/files/default_images/placeholder_rev.png')

    def __str__(self):
        return self.name
    

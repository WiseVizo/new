from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Food(models.Model):
    # connecting food table with user table using userid as foreign key
    user_name = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.CharField(max_length=600, default='https://www.foodista.com/sites/default/files/default_images/placeholder_rev.png')

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("food:details", kwargs={"pk": self.pk})

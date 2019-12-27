from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Food(models.Model):
    name = models.CharField(max_length=400)
    brand = models.CharField(max_length=400)
    categories = models.CharField(max_length=500,null=True)

    def __str__(self):
        return self.name

class Ingredient(models.Model):
    food = models.ForeignKey(Food, on_delete=models.CASCADE)
    name = models.CharField(max_length=1100)
    ingredient_num = models.IntegerField()

    def __str__(self):
        return self.name
    
class LogEntry(models.Model):
    person = models.ForeignKey(User, related_name='User', on_delete=models.CASCADE)
    category = models.CharField(max_length=20, choices=[('Food','Food'),('Reaction','Reaction')])
    log_date = models.DateTimeField()
    item = models.ForeignKey(Food, on_delete=models.CASCADE)



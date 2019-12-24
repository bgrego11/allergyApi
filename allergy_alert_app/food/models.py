from django.db import models

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
    


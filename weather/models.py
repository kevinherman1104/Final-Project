from django.db import models

# Create your models here.
class NameCity(models.Model):
    name_of_city = models.CharField(max_length= 25) # To input name of cities
    
    def __str__(self):
        return self.name_of_city # return the name of cities 

    class Meta:
        verbose_name_plural = "cities" #we then make migrations and migrate this so we have the sam exact code in 0001_initial.py file

    

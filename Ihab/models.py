from django.db import models

# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=60)
    age= models.IntegerField()
    email= models.CharField(max_length=160)

    def __str__(self):
        return self.name + "   "+str(self.age)


from django.db import models

# Create your models here.

class Student(models.Model):
    firstname = models.CharField(max_length = 200)
    lastname = models.CharField(max_length= 200)
    age = models.IntegerField()
    grade = models.CharField(max_length= 10)
    gender = models.CharField(max_length= 10)
    
    
    def __str__(self):
        return self.firstname + ' ' + self.lastname
    
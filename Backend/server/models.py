from django.db import models


class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    age = models.IntegerField()


    def __str__(self) -> str:
        return self.email
        
        
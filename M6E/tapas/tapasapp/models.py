# Michelle Clare Que, 243687; Nathan Riley Sy, 244311; Andrew Gabriel Zapico, 246798
# April 15, 2026

'''
I hereby attest to the truth of the following facts:

I have not discussed the Python language code in my program with anyone
other than my instructor or the teaching assistants assigned to this course.

I have not used Python language code obtained from another student, or
any other unauthorized source, either modified or unmodified.

If any Python language code or documentation used in my program was
obtained from another source, such as a textbook or course notes, that has been clearly noted with proper citation in the
comments of my program.
'''

from django.db import models

# Create your models here.

class Dish(models.Model):
    name = models.CharField(max_length=300)
    prep_time = models.IntegerField()
    cook_time = models.IntegerField()
    objects = models.Manager()

    def __str__(self):
        return str(self.pk) + ": " + self.name

class Account(models.Model):
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100)

    def getUsername(self):
        return self.username

    def getPassword(self):
        return self.password

    def __str__(self):
        return self.username
    
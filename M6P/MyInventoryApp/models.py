# Michelle Clare Que, 243687; Nathan Riley Sy, 244311; Andrew Gabriel Zapico, 246798
# April 13, 2026

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
from django.utils import timezone

# Create your models here.

class Supplier(models.Model):
    Name = models.CharField(max_length=300)
    City = models.CharField(max_length=300)
    Country = models.CharField(max_length=300)
    Created_At = models.DateTimeField(blank=True, null=True)
    objects = models.Manager()

    def getName(self):
        return self.Name

    def __str__(self):
        return "{}, - {}, {} created at: {}".format(self.Name, self.City, self.Country, self.Created_At)

class WaterBottle(models.Model):
    SKU = models.CharField(max_length=300)
    Brand = models.CharField(max_length=300)
    Cost = models.DecimalField(max_digits=100, decimal_places=2)
    Size = models.CharField(max_length=300)
    Mouth_Size = models.CharField(max_length=300)
    Color = models.CharField(max_length=300)
    Supplied_by = models.ForeignKey(Supplier,on_delete=models.CASCADE)
    Current_Quantity = models.IntegerField()

    objects = models.Manager()

    def __str__(self):
        return "{}: {}, {}, {}, {}, supplied by {}, {} : {}".format(self.SKU, self.Brand, self.Mouth_Size, self.Size, self.Color, self.Supplied_by, self.Cost, self.Current_Quantity)

class Account(models.Model):
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100)

    def getUsername(self):
        return self.username

    def getPassword(self):
        return self.password

    def __str__(self):
        return self.username
from django.db import models
from django import forms
# Create your models here.
CLASS_CHOICES = [
    ("ICS-P1", "ICS-Part1"),
    ("ICS-P2", "ICS-Part2"),
    ("M-P1", "MEDICAL-Part1"),
    ("M-P2", "MEDICAL-Part2"),
    ("NM-P1", "NON-MEDICAL-Part1"),
    ("NM-P2", "NON-MEDICAL-Part2"),
]


class Student(models.Model):
    first_name = models.TextField(max_length=30, null=False, blank=False)
    last_name = models.TextField(max_length=30, null=False, blank=False)
    date_of_birth = models.DateField(null=False, blank=False, auto_now_add=False, auto_now=False)
    student_class = models.CharField(max_length=6, choices=CLASS_CHOICES)
    roll_number = models.PositiveSmallIntegerField(default=1, blank=False, null=False) 
    fee = models.BigIntegerField(blank=False, null=False)
    join = models.DateField(null=True, blank=True, auto_now_add=True)
    pass_matric = models.BooleanField(default=True)
    
    def __str__(self):
        return f"{self.roll_number} - {self.first_name} - {self.last_name} - {self.join} - {self.student_class}"


    







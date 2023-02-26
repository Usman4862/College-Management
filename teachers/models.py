from django.db import models
# Create your models here.
TEACHER_CLASS = {
    ("ICS-P1", "ICS-PART1"),
    ("ICS-P2", "ICS-PART2"),
    ("M-P1", "MEDICAL-PART1"),
    ("M-P2", "MEDICAL-PART2"),
    ("NM-P1", "NON-MEDICAL-PART2"),
    ("NM-P2", "NON-MEDICAL-PART2"),
}
class Teacher(models.Model):
    first_name = models.CharField(max_length= 30, null=False, blank=False)
    last_name = models.CharField(max_length= 30, null=False, blank=False)
    date_of_birth = models.DateTimeField(auto_now_add=False, auto_now=False, null=True, blank=True)
    teacher_class = models.CharField(max_length=10, choices=TEACHER_CLASS)
    joining_date = models.DateField(auto_now_add=True)
    contact_number = models.PositiveBigIntegerField(blank=False, null=False)
    still_joined = models.BooleanField(default=True)
    teacher_id = models.BigAutoField(primary_key=True)    


SALARY_CHOICE = {
    ("N", "NO"),
    ("Y", "YES"),
}
class Salary(models.Model):
    weekly_hours = models.SmallIntegerField(default=0, verbose_name="Weekly Duty Hours")
    paying_in_hours = models.SmallIntegerField(default=0)
    paying_amount = models.PositiveIntegerField(default=0, verbose_name='Salary')
    last_paid = models.DateField(auto_now_add=True, auto_now=False)
    current_month_amount = models.CharField(max_length=2, verbose_name='Is Current Month Salary Payed?', choices=SALARY_CHOICE, default="YES")
    class meta:
        abstract = True
        verbose_name = "Salary"
        verbose_name_plural = "Salary"
        

    

        

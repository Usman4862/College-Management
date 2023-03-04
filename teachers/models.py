from django.db import models
from django.core.exceptions import ValidationError
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
    class GenderChoice(models.TextChoices):
        MALE =  "M", ("Male")
        FEMALE = "F", ("Female")
        OTHERS = "O", ("Others")


    first_name = models.CharField(max_length= 30, null=False, blank=False)
    last_name = models.CharField(max_length= 30, null=False, blank=False)
    date_of_birth = models.DateTimeField(auto_now_add=False, auto_now=False, null=True, blank=True)
    teacher_class = models.CharField(max_length=10, choices=TEACHER_CLASS)
    joining_date = models.DateField(auto_now_add=True)
    contact_number = models.IntegerField(blank=True, null=True, default=8989889)
    still_joined = models.BooleanField(default=True)
    gender = models.CharField(max_length=25, choices=GenderChoice.choices)

    def __str__(self) -> str:
        return f"{self.first_name}"


class Salary(models.Model):
    class BankChoice(models.TextChoices):
        BANK_OF_PUNJAB = "POB", ("Bank of Punjab")
        HABIB_BANK = "HB", ("Habib Bank")
        MEEZAN_BANK = "MZB", ("Meezan Bank")
        ALFALAH_BANK = "ALB", ("Alfalah Bank")

    def validate(account_number):
        if len(str(account_number)) != "14":
            raise ValidationError("%(account_number) must have 14 digits", params={account_number: account_number})

    teacher = models.ForeignKey(Teacher, on_delete=models.PROTECT)
    basic_salary = models.PositiveIntegerField(default=0, verbose_name="Salary")
    specail_allowances = models.PositiveIntegerField(default=0, verbose_name="Allowances", help_text="Enter Allowances")
    bank = models.CharField(max_length=25, choices=BankChoice.choices)
    account_number = models.PositiveIntegerField(default=None, validators=[validate])
    

    class Meta:
        verbose_name = "Salary"
        verbose_name_plural = "Salaries"
    

    def __str__(self) -> str:
        return f"{self.teacher}"
 

# Generated by Django 4.1.7 on 2023-02-16 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0003_alter_student_date_of_birth'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='roll_number',
            field=models.PositiveSmallIntegerField(unique=True),
        ),
    ]

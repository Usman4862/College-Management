# Generated by Django 4.1.7 on 2023-02-16 19:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0004_alter_student_roll_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='roll_number',
            field=models.PositiveSmallIntegerField(default=1, unique=True),
        ),
    ]

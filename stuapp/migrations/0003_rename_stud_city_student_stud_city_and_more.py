# Generated by Django 4.1.5 on 2023-01-11 04:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stuapp', '0002_student'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='stud_City',
            new_name='Stud_City',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='stud_Course',
            new_name='Stud_Course',
        ),
    ]

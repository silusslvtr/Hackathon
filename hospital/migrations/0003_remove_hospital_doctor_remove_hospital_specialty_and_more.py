# Generated by Django 5.0.1 on 2024-01-19 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0002_alter_doctor_specialty'),
        ('hospital', '0002_alter_hospital_doctor'),
        ('specialty', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hospital',
            name='doctor',
        ),
        migrations.RemoveField(
            model_name='hospital',
            name='specialty',
        ),
        migrations.AddField(
            model_name='hospital',
            name='doctor',
            field=models.ManyToManyField(to='doctor.doctor'),
        ),
        migrations.AddField(
            model_name='hospital',
            name='specialty',
            field=models.ManyToManyField(to='specialty.specialty'),
        ),
    ]
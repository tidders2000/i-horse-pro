# Generated by Django 3.1.3 on 2021-01-27 20:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appointment', '0003_appointment_link'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appointment',
            name='end',
        ),
    ]
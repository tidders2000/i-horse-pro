# Generated by Django 3.1.3 on 2021-01-20 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('training', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='traininglog',
            name='date',
            field=models.DateField(auto_now=True),
        ),
    ]

# Generated by Django 3.1.3 on 2021-03-09 22:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='wizard',
            field=models.BooleanField(default=True),
        ),
    ]
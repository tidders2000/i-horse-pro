# Generated by Django 3.1.3 on 2022-08-08 19:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('competing', '0011_auto_20220808_2033'),
    ]

    operations = [
        migrations.RenameField(
            model_name='competitionlog',
            old_name='notes',
            new_name='performance',
        ),
    ]

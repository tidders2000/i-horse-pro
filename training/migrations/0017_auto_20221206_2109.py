# Generated by Django 3.1.3 on 2022-12-06 21:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('training', '0016_auto_20220905_1612'),
    ]

    operations = [
        migrations.RenameField(
            model_name='traininglog',
            old_name='notes',
            new_name='homework',
        ),
    ]

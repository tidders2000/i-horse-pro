# Generated by Django 3.1.3 on 2021-01-17 17:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('horse', '0017_auto_20210117_1714'),
    ]

    operations = [
        migrations.RenameField(
            model_name='horse',
            old_name='Notes',
            new_name='notes',
        ),
    ]

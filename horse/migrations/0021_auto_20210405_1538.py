# Generated by Django 3.1.3 on 2021-04-05 14:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('horse', '0020_auto_20210206_1204'),
    ]

    operations = [
        migrations.RenameField(
            model_name='horse',
            old_name='markings',
            new_name='color',
        ),
    ]

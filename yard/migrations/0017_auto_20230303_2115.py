# Generated by Django 3.1.3 on 2023-03-03 21:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('yard', '0016_client_passport'),
    ]

    operations = [
        migrations.RenameField(
            model_name='client',
            old_name='passport',
            new_name='image',
        ),
    ]

# Generated by Django 3.1.3 on 2021-08-04 21:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_email'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='email',
            new_name='Register_email',
        ),
    ]

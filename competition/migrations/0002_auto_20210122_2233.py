# Generated by Django 3.1.3 on 2021-01-22 22:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('competition', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comphorse',
            name='competition',
        ),
        migrations.RemoveField(
            model_name='comphorse',
            name='horse',
        ),
        migrations.RemoveField(
            model_name='comphorse',
            name='user',
        ),
        migrations.DeleteModel(
            name='CompetitionLog',
        ),
        migrations.DeleteModel(
            name='Comphorse',
        ),
        migrations.DeleteModel(
            name='Venue',
        ),
    ]

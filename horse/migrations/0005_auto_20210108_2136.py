# Generated by Django 3.1.3 on 2021-01-08 21:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('horse', '0004_auto_20210108_2102'),
    ]

    operations = [
        migrations.AlterField(
            model_name='horse',
            name='photo',
            field=models.ImageField(blank=True, default='static/images/horse.jpeg', upload_to='media/images/horses'),
        ),
    ]

# Generated by Django 3.1.3 on 2021-02-02 20:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('horse', '0018_auto_20210117_1717'),
    ]

    operations = [
        migrations.AlterField(
            model_name='horse',
            name='photo',
            field=models.ImageField(blank=True, default='media/images/horses/horse.jpeg', upload_to='media/images/horses'),
        ),
    ]

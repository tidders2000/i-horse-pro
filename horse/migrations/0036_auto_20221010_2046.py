# Generated by Django 3.1.3 on 2022-10-10 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('horse', '0035_auto_20220919_1733'),
    ]

    operations = [
        migrations.AlterField(
            model_name='horse',
            name='Arrived',
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name='horse',
            name='Left',
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name='horse',
            name='breed',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='horse',
            name='height',
            field=models.CharField(blank=True, max_length=4),
        ),
        migrations.AlterField(
            model_name='horse',
            name='pedigree',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]

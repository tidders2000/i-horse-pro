# Generated by Django 3.1.3 on 2022-09-19 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('horse', '0034_auto_20220918_2131'),
    ]

    operations = [
        migrations.AlterField(
            model_name='horse',
            name='Arrived',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='horse',
            name='Dob',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='horse',
            name='Left',
            field=models.DateField(),
        ),
    ]
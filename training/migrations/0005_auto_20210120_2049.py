# Generated by Django 3.1.3 on 2021-01-20 20:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('training', '0004_auto_20210120_2038'),
    ]

    operations = [
        migrations.AlterField(
            model_name='traininglog',
            name='date',
            field=models.DateField(null=True),
        ),
    ]

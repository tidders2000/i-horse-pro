# Generated by Django 3.1.3 on 2021-01-09 22:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('horse', '0007_link_horse'),
    ]

    operations = [
        migrations.AlterField(
            model_name='link',
            name='link',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='link',
            name='organisation',
            field=models.CharField(max_length=100),
        ),
    ]

# Generated by Django 3.1.3 on 2021-01-24 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointment', '0002_auto_20210118_2045'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='link',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
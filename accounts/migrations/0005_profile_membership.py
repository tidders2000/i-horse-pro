# Generated by Django 3.1.3 on 2023-02-27 20:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20210804_2213'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='membership',
            field=models.CharField(default='Free', max_length=254),
        ),
    ]
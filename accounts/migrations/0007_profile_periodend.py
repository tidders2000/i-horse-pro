# Generated by Django 3.1.3 on 2023-03-19 21:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_profile_subid'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='periodEnd',
            field=models.DateField(null=True),
        ),
    ]
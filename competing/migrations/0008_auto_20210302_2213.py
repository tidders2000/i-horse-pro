# Generated by Django 3.1.3 on 2021-03-02 22:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('competing', '0007_auto_20210202_1659'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comphorse',
            old_name='performance',
            new_name='scores',
        ),
    ]

# Generated by Django 3.1.3 on 2021-01-10 20:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('horse', '0008_auto_20210109_2234'),
    ]

    operations = [
        migrations.AddField(
            model_name='horse',
            name='passport',
            field=models.ImageField(blank=True, default='/static/images/passport.jpg', upload_to='media/images/passport'),
        ),
    ]

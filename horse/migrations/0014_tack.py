# Generated by Django 3.1.3 on 2021-01-17 14:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('horse', '0013_auto_20210110_2108'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tack',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tacktype', models.CharField(choices=[('Saddle', 'Saddle'), ('Bit', 'Bit'), ('Bridle', 'Bridle'), ('Other', 'Other')], default='Saddle', max_length=40)),
                ('description', models.CharField(default='Description', max_length=256)),
                ('horse', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='horse.horse')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

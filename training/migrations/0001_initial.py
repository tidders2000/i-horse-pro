# Generated by Django 3.1.3 on 2021-01-20 18:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('horse', '0018_auto_20210117_1717'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomImages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('disipline', models.CharField(blank=True, choices=[('Dressage', 'Dressage'), ('ShowJumping', 'ShowJumping'), ('Eventing', 'Eventing'), ('PonyClub', 'PonyClub')], default='Dressage', max_length=100)),
                ('image', models.ImageField(blank=True, default='', upload_to='media/images/custom')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='TrainingLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('instructor', models.CharField(blank=True, max_length=100)),
                ('location', models.CharField(blank=True, max_length=100)),
                ('lightbulb', models.CharField(blank=True, max_length=100)),
                ('littlewins1', models.CharField(blank=True, max_length=100)),
                ('littlewins2', models.CharField(blank=True, max_length=100)),
                ('littlewins3', models.CharField(blank=True, max_length=100)),
                ('floorPlan', models.ImageField(blank=True, default='', upload_to='media/images/floorplan')),
                ('notes', models.TextField(blank=True, default='')),
                ('files', models.FileField(upload_to='media/uploads')),
                ('disipline', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='training.customimages')),
                ('horse', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='horse.horse')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Objectives',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('objective', models.CharField(blank=True, max_length=100)),
                ('Completed', models.BooleanField()),
                ('session', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='training.traininglog')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

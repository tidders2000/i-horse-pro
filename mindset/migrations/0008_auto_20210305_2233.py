# Generated by Django 3.1.3 on 2021-03-05 22:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mindset', '0007_auto_20210305_2218'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goals',
            name='performance_goal_1',
            field=models.TextField(blank=True, default='Performance Goal', max_length=256),
        ),
        migrations.AlterField(
            model_name='goals',
            name='performance_goal_2',
            field=models.TextField(blank=True, default='Performance Goal', max_length=256),
        ),
        migrations.AlterField(
            model_name='goals',
            name='performance_goal_3',
            field=models.TextField(blank=True, default='Performance Goal', max_length=256),
        ),
        migrations.AlterField(
            model_name='goals',
            name='process_goal_1',
            field=models.TextField(blank=True, default='Process Goal', max_length=256),
        ),
        migrations.AlterField(
            model_name='goals',
            name='process_goal_2',
            field=models.TextField(blank=True, default='Process Goal', max_length=256),
        ),
        migrations.AlterField(
            model_name='goals',
            name='process_goal_3',
            field=models.TextField(blank=True, default='Process Goal', max_length=256),
        ),
        migrations.AlterField(
            model_name='goals',
            name='process_goal_4',
            field=models.TextField(blank=True, default='Process Goal', max_length=256),
        ),
    ]
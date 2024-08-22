# Generated by Django 5.1 on 2024-08-22 05:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teethapp', '0010_calendarmodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='calendarmodel',
            name='end_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='calendarmodel',
            name='start_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
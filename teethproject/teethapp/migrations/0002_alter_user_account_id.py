# Generated by Django 5.1 on 2024-08-14 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teethapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='account_id',
            field=models.CharField(max_length=254, unique=True, verbose_name='account_id'),
        ),
    ]

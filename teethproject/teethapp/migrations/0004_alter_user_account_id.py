# Generated by Django 5.1 on 2024-08-15 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teethapp', '0003_alter_user_account_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='account_id',
            field=models.CharField(max_length=10, verbose_name='account_id'),
        ),
    ]
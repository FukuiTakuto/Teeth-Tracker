# Generated by Django 5.1 on 2024-08-16 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teethapp', '0004_alter_user_account_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='MediaUploadModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('img', models.ImageField(upload_to='')),
            ],
        ),
    ]

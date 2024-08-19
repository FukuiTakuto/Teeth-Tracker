# Generated by Django 5.1 on 2024-08-19 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teethapp', '0007_mediauploadmodel_memo_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='mediauploadmodel',
            name='tag',
            field=models.CharField(blank=True, choices=[('front', '前'), ('right', '右'), ('left', '左'), ('top', '上'), ('bottom', '下')], max_length=10),
        ),
    ]

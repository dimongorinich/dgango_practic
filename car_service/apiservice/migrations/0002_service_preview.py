# Generated by Django 4.1.7 on 2024-01-17 12:43

import apiservice.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apiservice', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='preview',
            field=models.ImageField(null=True, upload_to=apiservice.models.service_preview_directory_path),
        ),
    ]

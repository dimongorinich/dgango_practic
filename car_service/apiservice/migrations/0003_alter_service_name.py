# Generated by Django 4.1.7 on 2024-01-17 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apiservice', '0002_service_preview'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='name',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]

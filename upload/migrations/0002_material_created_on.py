# Generated by Django 4.0.3 on 2022-07-23 21:44

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('upload', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='material',
            name='created_on',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]

# Generated by Django 4.1.2 on 2022-12-08 03:06

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('lessons', '0010_lesson_invoice'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lesson',
            name='start_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]

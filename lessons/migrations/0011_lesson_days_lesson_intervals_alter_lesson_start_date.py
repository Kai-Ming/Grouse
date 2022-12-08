# Generated by Django 4.1.2 on 2022-12-08 00:36

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('lessons', '0010_lesson_invoice'),
    ]

    operations = [
        migrations.AddField(
            model_name='lesson',
            name='days',
            field=models.PositiveIntegerField(choices=[(1, 'Monday'), (2, 'Tuesday'), (3, 'Wednesday'), (4, 'Thursday'), (5, 'Friday'), (6, 'Saturday'), (7, 'Sunday')], default=1),
        ),
        migrations.AddField(
            model_name='lesson',
            name='intervals',
            field=models.PositiveIntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='start_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]

# Generated by Django 4.1.3 on 2022-11-21 22:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lessons', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='user_type',
            field=models.PositiveSmallIntegerField(choices=[(1, 'student'), (2, 'adult'), (3, 'teacher'), (4, 'admin'), (5, 'superadmin')], default=5),
        ),
    ]
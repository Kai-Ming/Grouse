# Generated by Django 4.1.2 on 2022-12-08 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lessons', '0011_alter_lesson_start_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lesson',
            name='fulfilled',
            field=models.BooleanField(choices=[(True, 'Accept'), (False, 'Reject')], default=False),
        ),
    ]

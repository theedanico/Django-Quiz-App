# Generated by Django 4.0.3 on 2022-12-08 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0007_quiz_time_limit_mins'),
    ]

    operations = [
        migrations.AddField(
            model_name='score',
            name='time',
            field=models.PositiveIntegerField(default=0),
        ),
    ]

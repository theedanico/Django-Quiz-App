# Generated by Django 4.0.3 on 2022-12-08 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0006_score'),
    ]

    operations = [
        migrations.AddField(
            model_name='quiz',
            name='time_limit_mins',
            field=models.PositiveIntegerField(default=0),
            preserve_default=False,
        ),
    ]

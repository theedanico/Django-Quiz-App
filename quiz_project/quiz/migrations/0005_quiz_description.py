# Generated by Django 4.0.3 on 2022-04-12 06:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0004_alter_profile_avatar_question_option'),
    ]

    operations = [
        migrations.AddField(
            model_name='quiz',
            name='description',
            field=models.CharField(default='No description added', max_length=500),
        ),
    ]

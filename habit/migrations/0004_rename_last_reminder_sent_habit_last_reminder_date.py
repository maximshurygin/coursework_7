# Generated by Django 4.2.7 on 2023-11-19 10:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('habit', '0003_habit_last_reminder_sent'),
    ]

    operations = [
        migrations.RenameField(
            model_name='habit',
            old_name='last_reminder_sent',
            new_name='last_reminder_date',
        ),
    ]

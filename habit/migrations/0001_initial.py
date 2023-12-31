# Generated by Django 4.2.7 on 2023-11-14 09:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Habit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=200, verbose_name='Место')),
                ('time', models.TimeField(verbose_name='Время')),
                ('action', models.CharField(max_length=200, verbose_name='Действие')),
                ('is_pleasant', models.BooleanField(default=False, verbose_name='Признак приятной привычки')),
                ('frequency', models.IntegerField(default=1, verbose_name='Периодичность в днях')),
                ('reward', models.CharField(max_length=150, verbose_name='Вознаграждение')),
                ('duration', models.DurationField(verbose_name='Время на выполнение')),
                ('is_public', models.BooleanField(default=False, verbose_name='Признак публичности')),
                ('related_habit', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='habit.habit', verbose_name='Связанная привычка')),
            ],
            options={
                'verbose_name': 'Привычка',
                'verbose_name_plural': 'Привычки',
            },
        ),
    ]

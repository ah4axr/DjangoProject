# Generated by Django 3.0.2 on 2020-07-09 02:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Coach',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('birth_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('game_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('arena', models.CharField(max_length=35)),
                ('game_type', models.CharField(max_length=25)),
                ('home_team', models.CharField(max_length=35)),
                ('away_team', models.CharField(max_length=35)),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('birth_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('position', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=25)),
                ('city', models.CharField(max_length=25)),
                ('home_arena', models.CharField(max_length=35)),
            ],
        ),
        migrations.CreateModel(
            name='Search',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('player_name', models.CharField(blank=True, max_length=41, null=True)),
                ('team_name', models.CharField(blank=True, max_length=25, null=True)),
                ('coach_name', models.CharField(blank=True, max_length=41, null=True)),
                ('game_date', models.DateTimeField(blank=True, null=True)),
                ('player_age', models.CharField(blank=True, max_length=3, null=True)),
                ('position', models.CharField(blank=True, max_length=25, null=True)),
                ('city', models.CharField(blank=True, max_length=25, null=True)),
                ('highlight_type', models.CharField(blank=True, max_length=30, null=True)),
                ('user', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Highlight',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('highlight_type', models.CharField(max_length=30)),
                ('game_id', models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='highlights.Game')),
                ('player_id', models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='highlights.Player')),
            ],
        ),
    ]
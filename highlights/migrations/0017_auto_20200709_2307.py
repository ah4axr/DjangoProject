# Generated by Django 3.0.2 on 2020-07-10 03:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('highlights', '0016_auto_20200709_2245'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='search',
            name='coach_lname',
        ),
        migrations.RemoveField(
            model_name='search',
            name='team_city',
        ),
        migrations.RemoveField(
            model_name='search',
            name='team_name',
        ),
    ]

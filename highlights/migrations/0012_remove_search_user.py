# Generated by Django 3.0.2 on 2020-07-09 02:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('highlights', '0011_auto_20200708_2200'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='search',
            name='user',
        ),
    ]

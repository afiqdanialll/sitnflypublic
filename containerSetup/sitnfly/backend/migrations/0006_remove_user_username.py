# Generated by Django 5.0.6 on 2024-06-30 19:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0005_remove_flight_arrival_date_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='username',
        ),
    ]
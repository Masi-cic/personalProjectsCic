# Generated by Django 5.0.7 on 2024-07-24 09:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('allfunctions', '0005_alter_room_entry_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='room',
            name='entry_date',
        ),
    ]

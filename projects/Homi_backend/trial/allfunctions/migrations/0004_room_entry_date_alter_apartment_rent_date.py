# Generated by Django 5.0.7 on 2024-07-24 09:17

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('allfunctions', '0003_apartment_rent_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='entry_date',
            field=models.DateField(default=datetime.datetime(2024, 7, 24, 9, 17, 1, 104903, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='apartment',
            name='rent_date',
            field=models.PositiveSmallIntegerField(default=1, help_text='Day of the month when rent is due (e.g., 1 for 1st)'),
        ),
    ]
# Generated by Django 5.0.7 on 2024-07-30 09:51

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('allfunctions', '0011_remove_apartment_rent_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='room_images',
            field=models.ImageField(default='Homi rooms', upload_to='room_images/'),
        ),
        migrations.AlterField(
            model_name='complaint',
            name='date_field',
            field=models.DateField(verbose_name=datetime.datetime(2024, 7, 30, 9, 51, 59, 130292, tzinfo=datetime.timezone.utc)),
        ),
    ]

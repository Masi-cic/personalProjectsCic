# Generated by Django 5.0.7 on 2024-07-24 13:18

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('allfunctions', '0009_room_tenant_alter_complaint_date_field'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='room',
            name='room_images',
        ),
        migrations.AlterField(
            model_name='complaint',
            name='date_field',
            field=models.DateField(verbose_name=datetime.datetime(2024, 7, 24, 13, 18, 36, 842828, tzinfo=datetime.timezone.utc)),
        ),
        migrations.CreateModel(
            name='RoomImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='room_images/')),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='allfunctions.room')),
            ],
        ),
    ]
# Generated by Django 5.0.7 on 2024-07-24 09:31

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('allfunctions', '0006_remove_room_entry_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Complaint',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_field', models.DateField(verbose_name=datetime.datetime(2024, 7, 24, 9, 31, 0, 778247, tzinfo=datetime.timezone.utc))),
                ('complaint_body', models.TextField()),
                ('status', models.BooleanField()),
                ('landlord', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='landlord_complaint', to='allfunctions.landlord')),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='room_complaint', to='allfunctions.room')),
                ('tenant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tenant_complaint', to='allfunctions.tenant')),
            ],
        ),
    ]

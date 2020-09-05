# Generated by Django 3.1.1 on 2020-09-05 10:39

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('bookmyticket_app', '0003_booking_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='booking_uuid',
            field=models.UUIDField(default=uuid.UUID('90e3b09c-13d9-4a7b-b028-50c71a3d18e4')),
        ),
    ]
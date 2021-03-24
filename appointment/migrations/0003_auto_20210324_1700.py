# Generated by Django 3.1.7 on 2021-03-24 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointment', '0002_appointment_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='status',
            field=models.CharField(choices=[('none', 'NONE'), ('pending', 'PENDING'), ('booked', 'BOOKED'), ('cancelled', 'CANCELLED')], default='none', max_length=10),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='time',
            field=models.DateTimeField(unique=True),
        ),
    ]
# Generated by Django 3.1.7 on 2021-03-29 14:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0001_initial'),
        ('appointment', '0003_auto_20210324_1700'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='doctor_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='doctor.doctor'),
        ),
    ]

# Generated by Django 4.2.7 on 2024-01-09 07:50

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('revear_app', '0002_taskdata_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taskdata',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2024, 1, 9, 7, 50, 49, 380041, tzinfo=datetime.timezone.utc), null=True),
        ),
    ]

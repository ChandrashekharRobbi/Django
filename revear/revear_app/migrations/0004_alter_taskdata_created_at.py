# Generated by Django 4.2.7 on 2024-01-09 16:35

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('revear_app', '0003_alter_taskdata_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taskdata',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2024, 1, 9, 16, 35, 48, 202905, tzinfo=datetime.timezone.utc), null=True),
        ),
    ]

# Generated by Django 5.1.1 on 2024-09-18 09:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ages', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agesverification',
            name='upload_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2024, 9, 18, 14, 8, 33, 294922)),
        ),
    ]

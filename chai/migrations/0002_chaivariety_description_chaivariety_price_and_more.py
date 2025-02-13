# Generated by Django 5.0.6 on 2024-06-06 15:22

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chai', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='chaivariety',
            name='description',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='chaivariety',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5),
        ),
        migrations.AlterField(
            model_name='chaivariety',
            name='date_added',
            field=models.DateTimeField(default=datetime.datetime(2024, 6, 6, 15, 22, 7, 712184, tzinfo=datetime.timezone.utc)),
        ),
    ]

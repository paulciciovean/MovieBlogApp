# Generated by Django 3.2.5 on 2021-08-13 17:25

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0031_auto_20210813_1653'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='rating_count',
            field=models.ImageField(blank=True, default=0, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='review',
            name='date',
            field=models.DateField(blank=True, default=datetime.datetime(2021, 8, 13, 17, 25, 59, 584654)),
        ),
    ]

# Generated by Django 3.2.5 on 2021-08-10 11:38

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0025_alter_review_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='date',
            field=models.DateField(blank=True, default=datetime.datetime(2021, 8, 10, 11, 38, 51, 489980)),
        ),
    ]

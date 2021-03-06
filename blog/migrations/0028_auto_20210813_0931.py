# Generated by Django 3.2.5 on 2021-08-13 09:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0027_auto_20210811_1857'),
    ]

    operations = [
        migrations.AddField(
            model_name='rating',
            name='star1',
            field=models.ImageField(blank=True, default='images/orangestar.png', null=True, upload_to='images/'),
        ),
        migrations.AddField(
            model_name='rating',
            name='star2',
            field=models.ImageField(blank=True, default='images/bluestar.jpeg', null=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='review',
            name='date',
            field=models.DateField(blank=True, default=datetime.datetime(2021, 8, 13, 9, 31, 0, 943520)),
        ),
    ]

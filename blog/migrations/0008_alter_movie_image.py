# Generated by Django 3.2.5 on 2021-07-29 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20210729_1710'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='image',
            field=models.ImageField(null=True, upload_to='images/'),
        ),
    ]

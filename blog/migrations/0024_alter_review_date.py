# Generated by Django 3.2.5 on 2021-08-10 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0023_auto_20210810_1132'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='date',
            field=models.DateField(auto_now_add=True),
        ),
    ]
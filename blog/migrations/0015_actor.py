# Generated by Django 3.2.5 on 2021-08-06 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0014_alter_watchlist_user_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(max_length=100)),
                ('lastName', models.CharField(max_length=100)),
                ('birthYear', models.IntegerField(default=1930)),
                ('description', models.TextField()),
                ('image', models.ImageField(blank=True, default='images/default.png', null=True, upload_to='images/')),
            ],
        ),
    ]

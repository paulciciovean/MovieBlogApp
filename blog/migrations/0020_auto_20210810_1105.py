# Generated by Django 3.2.5 on 2021-08-10 11:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0019_auto_20210810_1059'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='movie',
        ),
        migrations.AddField(
            model_name='review',
            name='movie',
            field=models.ForeignKey(default=404, on_delete=django.db.models.deletion.CASCADE, to='blog.movie'),
            preserve_default=False,
        ),
    ]
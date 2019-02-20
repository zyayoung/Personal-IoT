# Generated by Django 2.1.4 on 2019-02-20 00:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monitor', '0003_auto_20190219_2227'),
    ]

    operations = [
        migrations.AddField(
            model_name='slot',
            name='scale_factor',
            field=models.FloatField(blank=True, default=1),
        ),
        migrations.AddField(
            model_name='slot',
            name='unit',
            field=models.CharField(blank=True, default='', max_length=64),
        ),
    ]

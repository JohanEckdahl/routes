# Generated by Django 2.0.1 on 2018-01-03 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('routes', '0003_auto_20180103_1207'),
    ]

    operations = [
        migrations.AlterField(
            model_name='route',
            name='name',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]

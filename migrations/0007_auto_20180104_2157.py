# Generated by Django 2.0.1 on 2018-01-04 20:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('routes', '0006_auto_20180104_0810'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='route',
            options={'get_latest_by': 'wall'},
        ),
    ]
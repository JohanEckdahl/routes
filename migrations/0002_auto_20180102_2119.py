# Generated by Django 2.0.1 on 2018-01-02 20:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('routes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='route',
            name='date_set',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='route',
            name='grade',
            field=models.CharField(blank=True, max_length=5),
        ),
        migrations.AlterField(
            model_name='route',
            name='name',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='route',
            name='setter',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]

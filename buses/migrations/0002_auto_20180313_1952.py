# Generated by Django 2.0.3 on 2018-03-13 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buses', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='line',
            name='line_voltage',
            field=models.IntegerField(default=3),
        ),
    ]

# Generated by Django 2.2.2 on 2019-08-13 23:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quickstart', '0003_auto_20190725_1315'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='guests_qty',
            field=models.IntegerField(blank=True),
        ),
    ]

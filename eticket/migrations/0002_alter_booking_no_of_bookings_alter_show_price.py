# Generated by Django 4.0.3 on 2022-03-12 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eticket', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='no_of_bookings',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='show',
            name='price',
            field=models.IntegerField(),
        ),
    ]

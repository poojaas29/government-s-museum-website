# Generated by Django 3.1.6 on 2022-03-15 06:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('eticket', '0005_auto_20220313_1345'),
    ]

    operations = [
        migrations.RenameField(
            model_name='booking_detail',
            old_name='date_of_visit',
            new_name='dov',
        ),
        migrations.RenameField(
            model_name='booking_detail',
            old_name='museum_name',
            new_name='museumname',
        ),
        migrations.RenameField(
            model_name='booking_detail',
            old_name='no_of_booking',
            new_name='nob',
        ),
        migrations.RenameField(
            model_name='booking_detail',
            old_name='time_slot',
            new_name='time',
        ),
    ]

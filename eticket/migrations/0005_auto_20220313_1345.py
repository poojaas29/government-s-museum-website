# Generated by Django 3.1.6 on 2022-03-13 08:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eticket', '0004_rename_no_of_bookings_booking_detail_no_of_booking_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='visitor',
            name='email',
        ),
        migrations.AlterField(
            model_name='booking_detail',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='visitor',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]

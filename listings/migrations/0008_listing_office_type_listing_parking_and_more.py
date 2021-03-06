# Generated by Django 4.0.2 on 2022-05-05 01:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0007_alter_listing_lot_size'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='office_type',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='listing',
            name='parking',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AddField(
            model_name='listing',
            name='residential_type',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='listing',
            name='warehouse_type',
            field=models.BooleanField(default=True),
        ),
    ]

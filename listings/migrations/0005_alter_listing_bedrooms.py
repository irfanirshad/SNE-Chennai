# Generated by Django 4.0.2 on 2022-03-01 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0004_alter_listing_lot_size'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='bedrooms',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]

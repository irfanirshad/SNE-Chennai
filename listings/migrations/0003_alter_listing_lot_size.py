# Generated by Django 4.0.2 on 2022-03-01 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0002_alter_listing_lot_size'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='lot_size',
            field=models.DecimalField(decimal_places=1, max_digits=5),
        ),
    ]

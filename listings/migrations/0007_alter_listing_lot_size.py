# Generated by Django 4.0.2 on 2022-03-01 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0006_alter_listing_bathrooms'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='lot_size',
            field=models.DecimalField(blank=True, decimal_places=1, default=0, max_digits=5),
        ),
    ]

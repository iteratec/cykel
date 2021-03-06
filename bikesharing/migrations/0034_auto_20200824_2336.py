# Generated by Django 2.2.15 on 2020-08-24 21:36

from django.db import migrations, models
from textwrap import dedent


class Migration(migrations.Migration):

    dependencies = [
        ("bikesharing", "0033_auto_20200818_1638"),
    ]

    operations = [
        migrations.AddField(
            model_name="bike",
            name="current_range_meters",
            field=models.FloatField(
                blank=True,
                default=None,
                help_text=dedent(
                    """\
                    If the corresponding vehicle_type definition for this vehicle
                    has a motor, then this field is required. This value represents
                    the furthest distance in meters that the vehicle can travel
                    without recharging or refueling with the vehicle's current
                    charge or fuel.
                    """
                ),
                null=True,
            ),
        ),
    ]

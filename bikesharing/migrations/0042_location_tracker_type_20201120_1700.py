# Generated by Django 3.1.2 on 2020-11-20 15:58

from django.db import migrations, models
import django.db.models.deletion


def create_and_assign_tracker_types(apps, schema_editor):
    LocationTracker = apps.get_model("bikesharing", "LocationTracker")
    LocationTrackerType = apps.get_model("bikesharing", "LocationTrackerType")
    used_tracker_types = []
    for tracker in LocationTracker.objects.order_by("tracker_type_str").distinct(
        "tracker_type_str"
    ):
        if tracker.tracker_type_str is not None:
            used_tracker_types.append(tracker.tracker_type_str)
    for tracker_type in used_tracker_types:
        tt = LocationTrackerType.objects.create(name=tracker_type)
        tt.save()
        LocationTracker.objects.filter(tracker_type_str=tracker_type).update(
            tracker_type_str=None, tracker_type=tt
        )


def remove_tracker_types(apps, schema_editor):
    LocationTracker = apps.get_model("bikesharing", "LocationTracker")
    LocationTrackerType = apps.get_model("bikesharing", "LocationTrackerType")
    for tt in LocationTrackerType.objects.all():
        LocationTracker.objects.filter(tracker_type=tt).update(
            tracker_type_str=tt.name, tracker_type=None
        )
        tt.delete()


class Migration(migrations.Migration):

    dependencies = [
        ("bikesharing", "0041_fix_permission_typo_20201026_1817"),
    ]

    operations = [
        migrations.CreateModel(
            name="LocationTrackerType",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        blank=True, default=None, max_length=255, null=True
                    ),
                ),
                (
                    "battery_voltage_warning",
                    models.FloatField(blank=True, default=None, null=True),
                ),
                (
                    "battery_voltage_critical",
                    models.FloatField(blank=True, default=None, null=True),
                ),
            ],
        ),
        migrations.RenameField(
            model_name="locationtracker",
            old_name="tracker_type",
            new_name="tracker_type_str",
        ),
        migrations.AddField(
            model_name="locationtracker",
            name="tracker_type",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                to="bikesharing.locationtrackertype",
            ),
        ),
        migrations.RunPython(create_and_assign_tracker_types, remove_tracker_types),
    ]

# Generated by Django 2.2.10 on 2020-06-05 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("bikesharing", "0024_auto_20200605_1632"),
    ]

    operations = [
        migrations.AddField(
            model_name="bikesharepreferences",
            name="gbfs_system_id",
            field=models.CharField(default="", max_length=255),
        ),
    ]

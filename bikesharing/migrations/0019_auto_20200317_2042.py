# Generated by Django 2.2.4 on 2020-03-17 19:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bikesharing', '0018_auto_20200204_2147'),
    ]

    operations = [
        migrations.AddField(
            model_name='locationtracker',
            name='tracker_status',
            field=models.CharField(choices=[('AC', 'Active'), ('IN', 'Inactive'), ('MI', 'Missing'), ('DE', 'Decommissioned')], default='IN', max_length=2),
        ),
        migrations.AlterField(
            model_name='location',
            name='bike',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.PROTECT, to='bikesharing.Bike'),
        ),
    ]

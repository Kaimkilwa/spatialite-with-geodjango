# Generated by Django 3.0.3 on 2020-02-14 08:48

import django.contrib.gis.db.models.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('testspatial', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='worldborder',
            name='geom',
            field=django.contrib.gis.db.models.fields.PointField(null=True, srid=4326),
        ),
    ]

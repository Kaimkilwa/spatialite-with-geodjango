# Generated by Django 3.0.3 on 2020-02-14 08:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('testspatial', '0003_auto_20200214_0850'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='worldborder',
            name='mpoly',
        ),
    ]
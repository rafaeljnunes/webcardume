# Generated by Django 2.0.7 on 2018-07-09 11:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0014_auto_20180709_1115'),
    ]

    operations = [
        migrations.RenameField(
            model_name='trade',
            old_name='offered_ammount',
            new_name='offered_amount',
        ),
    ]
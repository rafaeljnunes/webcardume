# Generated by Django 2.0.7 on 2018-07-12 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0020_product_featured'),
    ]

    operations = [
        migrations.AddField(
            model_name='trade',
            name='receiving_user',
            field=models.IntegerField(default=0),
        ),
    ]
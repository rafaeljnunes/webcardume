# Generated by Django 2.0.7 on 2018-07-08 14:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0006_message'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={},
        ),
        migrations.AlterField(
            model_name='message',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='webapp.Product'),
        ),
        migrations.AlterUniqueTogether(
            name='product',
            unique_together=set(),
        ),
    ]
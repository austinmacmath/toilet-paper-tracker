# Generated by Django 3.0.4 on 2020-03-26 21:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('welcome', '0002_auto_20200325_0313'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donor',
            name='longitude',
            field=models.DecimalField(decimal_places=6, max_digits=9),
        ),
        migrations.AlterField(
            model_name='recipient',
            name='longitude',
            field=models.DecimalField(decimal_places=6, max_digits=9),
        ),
    ]

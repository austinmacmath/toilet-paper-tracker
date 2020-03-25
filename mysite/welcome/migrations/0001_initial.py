# Generated by Django 3.0.4 on 2020-03-25 03:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Donor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('quantity', models.PositiveIntegerField(default=0)),
                ('latitude', models.DecimalField(decimal_places=6, max_digits=8)),
                ('longitude', models.DecimalField(decimal_places=6, max_digits=8)),
                ('points', models.PositiveIntegerField(default=0)),
                ('status', models.CharField(max_length=200)),
                ('join_date', models.DateTimeField(verbose_name='date joined')),
            ],
        ),
        migrations.CreateModel(
            name='Recipient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('request', models.IntegerField(default=1)),
                ('latitude', models.DecimalField(decimal_places=6, max_digits=8)),
                ('longitude', models.DecimalField(decimal_places=6, max_digits=8)),
                ('join_date', models.DateTimeField(verbose_name='date joined')),
                ('donor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='welcome.Donor')),
            ],
        ),
    ]

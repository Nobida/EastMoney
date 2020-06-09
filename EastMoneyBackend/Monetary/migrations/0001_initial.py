# Generated by Django 2.1.7 on 2020-06-09 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Monetary',
            fields=[
                ('fcode', models.AutoField(max_length=16, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(default='', max_length=32)),
                ('value', models.CharField(default='', max_length=32)),
                ('annualized_rate_7', models.CharField(default='', max_length=32)),
                ('annualized_rate_14', models.CharField(default='', max_length=32)),
                ('annualized_rate_28', models.CharField(default='', max_length=32)),
                ('starting_amount', models.IntegerField(max_length=8)),
                ('score', models.IntegerField(max_length=8)),
                ('record_time', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
# Generated by Django 2.1.7 on 2020-06-16 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Monetary', '0004_auto_20200610_0750'),
    ]

    operations = [
        migrations.AddField(
            model_name='monetary',
            name='starting_amount',
            field=models.CharField(default='', max_length=8),
        ),
    ]
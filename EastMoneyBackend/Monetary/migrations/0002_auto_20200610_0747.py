# Generated by Django 2.1.7 on 2020-06-10 07:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Monetary', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='monetary',
            old_name='primary_key',
            new_name='primarys_key',
        ),
    ]
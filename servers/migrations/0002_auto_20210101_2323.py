# Generated by Django 3.1.4 on 2021-01-01 23:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('servers', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='hosts',
            options={'default_permissions': ()},
        ),
    ]

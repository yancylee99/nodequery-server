# Generated by Django 3.1.4 on 2021-01-03 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servers', '0005_auto_20210102_2121'),
    ]

    operations = [
        migrations.AddField(
            model_name='hosts',
            name='have_notice',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='hosts',
            name='last_notice_at',
            field=models.DateTimeField(null=True),
        ),
    ]

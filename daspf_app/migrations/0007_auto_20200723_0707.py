# Generated by Django 3.0.7 on 2020-07-23 04:07

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('daspf_app', '0006_auto_20200723_0659'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='News',
            new_name='Post',
        ),
    ]

# Generated by Django 3.0.7 on 2020-08-04 21:02

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('daspf_app', '0010_auto_20200804_1727'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='phone',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=128, null=True, region=None),
        ),
    ]

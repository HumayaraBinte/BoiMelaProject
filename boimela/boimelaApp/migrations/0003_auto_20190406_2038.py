# Generated by Django 2.1.7 on 2019-04-06 14:38

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('boimelaApp', '0002_auto_20190406_2013'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Books',
            new_name='Book',
        ),
        migrations.RenameModel(
            old_name='Stalls',
            new_name='Stall',
        ),
    ]

# Generated by Django 2.2 on 2019-04-12 21:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boimelaApp', '0006_auto_20190409_1220'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stall',
            name='stall_type',
            field=models.CharField(choices=[('Book', 'Book'), ('Food', 'Food')], default='Type N/A', max_length=2),
        ),
    ]

# Generated by Django 3.2.11 on 2022-01-12 02:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apiservice', '0005_auto_20220112_1039'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='protocol',
            table='apiservice_protocol',
        ),
    ]

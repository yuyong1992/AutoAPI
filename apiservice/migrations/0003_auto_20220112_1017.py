# Generated by Django 3.2.11 on 2022-01-12 02:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apiservice', '0002_auto_20220112_1009'),
    ]

    operations = [
        migrations.AddField(
            model_name='result',
            name='update_time',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='api',
            name='create_time',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='api',
            name='update_time',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='case',
            name='create_time',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='case',
            name='update_time',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='collection',
            name='create_time',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='collection',
            name='update_time',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='result',
            name='create_time',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
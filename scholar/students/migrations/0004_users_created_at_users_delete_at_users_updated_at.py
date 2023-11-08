# Generated by Django 4.2.6 on 2023-11-08 01:00

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0003_identificacion_types_remove_users_created_at_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='users',
            name='delete_at',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='users',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
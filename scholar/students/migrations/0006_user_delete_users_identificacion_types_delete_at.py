# Generated by Django 4.2.6 on 2023-11-15 00:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0005_remove_identificacion_types_delete_at'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=250)),
                ('status', models.BooleanField(default=True, null=True)),
                ('created_at', models.DateTimeField(default=datetime.datetime.now)),
                ('updated_at', models.DateTimeField(default=datetime.datetime.now)),
                ('delete_at', models.DateTimeField(null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Users',
        ),
        migrations.AddField(
            model_name='identificacion_types',
            name='delete_at',
            field=models.DateTimeField(null=True),
        ),
    ]
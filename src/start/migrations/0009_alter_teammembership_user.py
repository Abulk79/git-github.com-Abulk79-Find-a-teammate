# Generated by Django 5.0.1 on 2024-04-22 08:04

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('start', '0008_invite_request_delete_reqinv'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teammembership',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]

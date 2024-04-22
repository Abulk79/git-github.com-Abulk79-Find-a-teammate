# Generated by Django 5.0.1 on 2024-04-20 13:53

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('start', '0003_remove_teammembership_ownership_team_owner_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='team',
            name='project',
        ),
        migrations.RemoveField(
            model_name='team',
            name='seeks',
        ),
        migrations.AddField(
            model_name='user',
            name='contacts',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='user',
            name='info',
            field=models.CharField(default='', max_length=4095),
        ),
        migrations.AlterField(
            model_name='teammembership',
            name='team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='start.team'),
        ),
        migrations.CreateModel(
            name='ReqInv',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('invite', models.BooleanField()),
                ('receiver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='receiver_foreign_key', to=settings.AUTH_USER_MODEL)),
                ('sender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sender_foreign_key', to=settings.AUTH_USER_MODEL)),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='start.team')),
            ],
        ),
        migrations.CreateModel(
            name='TeamAd',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project', models.CharField(max_length=1023)),
                ('requirements', models.CharField(max_length=1023)),
                ('team', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='start.team')),
            ],
        ),
        migrations.CreateModel(
            name='UserAd',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project', models.CharField(max_length=1023)),
                ('role', models.CharField(max_length=1023)),
                ('skills', models.CharField(max_length=2047)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

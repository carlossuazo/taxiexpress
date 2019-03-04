# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2019-02-27 00:38
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20190226_1838'),
        ('taxiadmin', '0006_auto_20190223_1905'),
    ]

    operations = [
        migrations.CreateModel(
            name='Passenger',
            fields=[
                ('person_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='core.Person')),
            ],
            bases=('core.person',),
        ),
        migrations.AlterUniqueTogether(
            name='vehicle',
            unique_together=set([('register',)]),
        ),
    ]

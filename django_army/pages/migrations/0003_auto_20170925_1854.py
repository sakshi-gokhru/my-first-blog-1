# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_aboutpage_portfoliopage_servicespage_teampage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aboutpage',
            name='description',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='aboutpage',
            name='heading',
            field=models.CharField(max_length=100, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='aboutpage',
            name='image',
            field=models.ForeignKey(related_name='+', on_delete=django.db.models.deletion.SET_NULL, blank=True, to='wagtailimages.Image', null=True),
        ),
        migrations.AlterField(
            model_name='aboutpage',
            name='subheading',
            field=models.CharField(max_length=100, null=True, blank=True),
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0019_delete_filter'),
        ('wagtailcore', '0040_page_draft_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='HomePage',
            fields=[
                ('page_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('banner_text', models.TextField(default='', max_length=255)),
                ('banner_text_heading', models.TextField(default='', max_length=255)),
                ('banner_image', models.ForeignKey(related_name='+', on_delete=django.db.models.deletion.SET_NULL, to='wagtailimages.Image', null=True)),
                ('portfolio_link', models.ForeignKey(related_name='+', on_delete=django.db.models.deletion.SET_NULL, to='wagtailcore.Page', null=True)),
                ('services_link', models.ForeignKey(related_name='+', on_delete=django.db.models.deletion.SET_NULL, to='wagtailcore.Page', null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
    ]

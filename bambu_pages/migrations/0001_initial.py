# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100, db_index=True)),
                ('slug', models.SlugField()),
                ('slug_hierarchical', models.CharField(unique=True, max_length=255, editable=False)),
                ('order', models.PositiveIntegerField(default=0, db_index=True)),
                ('order_hierarchical', models.CharField(max_length=255, editable=False)),
                ('title', models.CharField(max_length=255, null=True, blank=True)),
                ('subtitle', models.CharField(max_length=255, null=True, blank=True)),
                ('body', models.TextField(null=True, blank=True)),
                ('css', models.TextField(null=True, blank=True)),
                ('author', models.ForeignKey(related_name='pages', editable=False, to=settings.AUTH_USER_MODEL)),
                ('parent', models.ForeignKey(related_name='children', blank=True, to='bambu_pages.Page', null=True)),
            ],
            options={
                'ordering': ('order_hierarchical',),
                'db_table': 'pages_page',
            },
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-12 02:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mineral',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_filename', models.TextField(blank=True, default='')),
                ('formula', models.TextField(blank=True, default='')),
                ('optical_porperties', models.TextField(blank=True, default='')),
                ('cleavage', models.TextField(blank=True, default='')),
                ('image_caption', models.TextField(blank=True, default='')),
                ('streak', models.TextField(blank=True, default='')),
                ('name', models.TextField(blank=True, default='')),
                ('crystal_system', models.TextField(blank=True, default='')),
                ('group', models.TextField(blank=True, default='')),
                ('specific_gravity', models.TextField(blank=True, default='')),
                ('strunz_classification', models.TextField(blank=True, default='')),
                ('crystal_symmetry', models.TextField(blank=True, default='')),
                ('mohs_scale_hardness', models.TextField(blank=True, default='')),
                ('unit_cell', models.TextField(blank=True, default='')),
                ('refractive_index', models.TextField(blank=True, default='')),
                ('category', models.TextField(blank=True, default='')),
                ('luster', models.TextField(blank=True, default='')),
                ('color', models.TextField(blank=True, default='')),
                ('crystal_habit', models.TextField(blank=True, default='')),
                ('diaphaneity', models.TextField(blank=True, default='')),
            ],
        ),
    ]
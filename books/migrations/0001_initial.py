# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255, verbose_name=b'Tytu\xc5\x82')),
                ('slug', models.SlugField(unique=True, max_length=255, verbose_name=b'Odno\xc5\x9bnik')),
                ('book_image', models.ImageField(upload_to=b'images', verbose_name=b'Ok\xc5\x82adka ksi\xc4\x85\xc5\xbcki', blank=True)),
                ('text', models.TextField(verbose_name=b'Tre\xc5\x9b\xc4\x87')),
                ('posted_date', models.DateTimeField(auto_now_add=True, verbose_name=b'Data dodania')),
            ],
            options={
                'verbose_name': 'Ksi\u0105\u017cka',
                'verbose_name_plural': 'Ksi\u0105\u017cki',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100, verbose_name=b'Nazwa Kategorii')),
                ('slug', models.SlugField(unique=True, max_length=100, verbose_name=b'Odno\xc5\x9bnik')),
                ('icon', models.ImageField(upload_to=b'icons', verbose_name=b'Ikonka Kategorii', blank=True)),
            ],
            options={
                'verbose_name': 'Kategoria',
                'verbose_name_plural': 'Kategorie',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='book',
            name='categories',
            field=models.ManyToManyField(to='books.Category', verbose_name=b'Kategorie'),
            preserve_default=True,
        ),
    ]

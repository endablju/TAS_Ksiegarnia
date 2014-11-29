# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_book_autor'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='book_image',
        ),
        migrations.RemoveField(
            model_name='category',
            name='icon',
        ),
        migrations.AddField(
            model_name='book',
            name='price',
            field=models.CharField(default=1, max_length=20, verbose_name=b'Cena'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='book',
            name='quantity',
            field=models.CharField(default=-1996, max_length=20, verbose_name=b'Ilosc'),
            preserve_default=False,
        ),
    ]

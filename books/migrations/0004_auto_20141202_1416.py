# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_auto_20141129_1514'),
    ]

    operations = [
        migrations.CreateModel(
            name='Basket',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user', models.CharField(max_length=500, verbose_name=b'Nazwa uzytkownika')),
                ('title', models.CharField(max_length=255, verbose_name=b'Tytu\xc5\x82')),
                ('autor', models.CharField(max_length=255, verbose_name=b'Autor')),
                ('price', models.DecimalField(verbose_name=b'Cena', max_digits=5, decimal_places=2)),
                ('quantity', models.IntegerField(verbose_name=b'Ilosc')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='book',
            name='price',
            field=models.DecimalField(verbose_name=b'Cena', max_digits=5, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='book',
            name='quantity',
            field=models.IntegerField(verbose_name=b'Ilosc'),
        ),
    ]

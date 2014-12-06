# -*- coding: utf-8 -*

from django.db import models


class Category(models.Model):
    name = models.CharField('Nazwa Kategorii', max_length=100)
    slug = models.SlugField('Odnośnik', unique=True, max_length=100)
    #icon = models.ImageField('Ikonka Kategorii', upload_to='icons', blank=True)

    class Meta:
        verbose_name = "Kategoria"
        verbose_name_plural = "Kategorie"

    def __unicode__(self):
        return self.name


class Book(models.Model):
    title = models.CharField('Tytuł', max_length=255)
    autor = models.CharField('Autor', max_length=255)
    slug = models.SlugField('Odnośnik', max_length=255, unique=True)
    text = models.TextField(verbose_name='Treść')
    categories = models.ManyToManyField(Category, verbose_name='Kategorie')
    posted_date = models.DateTimeField('Data dodania', auto_now_add=True)
    price = models.DecimalField('Cena', max_digits=5, decimal_places=2)
    quantity = models.IntegerField('Ilosc')
	
    class Meta:
        verbose_name = "Książka"
        verbose_name_plural = "Książki"

    def __unicode__(self):
        return self.title
		
class Basket(models.Model):
	user = models.CharField('Nazwa uzytkownika', max_length = 500)
	title = models.CharField('Tytuł', max_length=255)
	autor = models.CharField('Autor', max_length=255)
	price = models.DecimalField('Cena', max_digits=5,decimal_places=2)
	quantity = models.IntegerField('Ilosc')

	
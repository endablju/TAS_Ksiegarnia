# _*_ coding: utf-8 _*_
from django import forms
import re
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User

class FormularzRejestracji(forms.Form):
	username = forms.CharField(label="Login:",max_length=30)
	email = forms.EmailField(label="Email:")
	password1 = forms.CharField(label="Hasło:",widget=forms.PasswordInput())
	password2 = forms.CharField(label="Powtórz hasło:",widget=forms.PasswordInput())
	phone = forms.CharField(label="Telefon:",max_length=20,required=False)
	#adres = forms.CharField(label="Adres:",max_length=100)
	#postCode = forms.CharField(label="Kod pocztowy:",max_length=20)
	#city = forms.CharField(label="Miasto:",max_length=100)
	log_on = forms.BooleanField(label="Logowanie po rejestracji:",required=False)
	
	def clean_password2(self):
		password1=self.cleaned_data['password1']
		password2=self.cleaned_data['password2']
		if password1==password2:
			return password2
		else:    
			raise forms.ValidationError("Hasła się różnią")
	
	def clean_username(self):
		username = self.cleaned_data['username']
		if not re.search(r'^\w+$',username):
			raise forms.ValidationError("Dopuszczalne są tylko cyfry, litery angielskie i _")
		try:
			User.objects.get(username=username)
		except ObjectDoesNotExist:
			return username
		raise forms.ValidationError("Taki użytkownik już istnieje")
		
		
		
class FormularzDodawaniaKsiazek(forms.Form):
	title = forms.CharField(label="Tytuł",max_length=300)
	autor = forms.CharField(label="Autor:")
	link = forms.CharField(label="Odnosnik:",max_length=100)
	#image = forms.ImageField(label="Okładka książki:")
	description = forms.CharField(label="Opis:",widget = forms.Textarea)
	#category = forms.ChoiceField(label="Kategoria:")
	price = forms.CharField(label="Cena:")
	quantity = forms.CharField(label="Ilosc:")
	
	
	
class FormularzDodawaniaKategorii(forms.Form):
		name = forms.CharField(label="Nazwa kategorii:",max_length=300)
		link = forms.CharField(label="Odnosnik:", max_length=300)
		#image = forms.ImageField(label="Ikona kategori:")

class FormularzWyszukiwania(forms.Form):
		name = forms.CharField(label="Szukaj:")
		
		
#http://bogdan.students.wmi.amu.edu.pl/education/python%20i%20django/Django_3.html
#http://moszust.prz-rzeszow.pl/Instrukcja%20Django%202.pdf
#http://www.django-rest-framework.org/tutorial/quickstart
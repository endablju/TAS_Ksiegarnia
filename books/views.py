# -*- coding: utf-8 -*-

from django.contrib.auth import logout
from django.http import HttpResponse,HttpResponseRedirect
from django.template.loader import get_template
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.contrib.auth.models import User
from rest_framework import viewsets
from books.models import *
from books.forms import *
from books.serializers import *
from jsonrpc import jsonrpc_method
import xmlrpclib

# Create an object to represent our server.
server_url = 'http://127.0.0.1:8001';
server = xmlrpclib.Server(server_url);

def index(request):
	template = get_template("index.html") 
	categories = Category.objects.all()
	books = Book.objects.all()
	variables=RequestContext(request,{'categories':categories, 'books':books})
	output = template.render(variables)
	return HttpResponse(output)

	
def register_page(request):
    if request.method == 'POST':
        form = FormularzRejestracji(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
              username=form.cleaned_data['username'],
              password=form.cleaned_data['password1'],
              email=form.cleaned_data['email'],
			  #adres=form.cleaned_data['adres'],
			  #postCode=form.cleaned_data['postCode'],
			  #city=form.cleaned_data['city']
            )
            user.last_name = form.cleaned_data['phone']
            user.save()
            if form.cleaned_data['log_on']:
                user = authenticate(username=form.cleaned_data['username'],password=form.cleaned_data['password1'])
                login(request,user)
                template = get_template("index.html")
                variables = RequestContext(request,{'user':user})
                output = template.render(variables)
                return HttpResponseRedirect("/") 
            else:    
                template = get_template("registration/register_success.html")
                variables = RequestContext(request,{'username':form.cleaned_data['username']})
                output = template.render(variables)
                return HttpResponse(output)            
    else:
        form = FormularzRejestracji()
    template = get_template("registration/register.html")    
    variables = RequestContext(request,{'form':form})
    output = template.render(variables)
    return HttpResponse(output)
	
def add_book_rpc(request):
	if request.method == 'POST':
		form = FormularzDodawaniaKsiazek(request.POST)
		if form.is_valid():
			title = request.POST['title']
			autor = request.POST['autor']
			slug = request.POST['link']
			text = request.POST['description']
			price = request.POST['price']
			quantity = request.POST['quantity']
			server.add_book(title,autor,slug,text,price,quantity)
			
			template = get_template("page/add_book_succes.html")    
			variables = RequestContext(request,{'form':form})
			output = template.render(variables)
			return HttpResponse(output)  
	else:
		form = FormularzDodawaniaKsiazek()    
	template = get_template("page/add_book.html")
	variables = RequestContext(request,{'form':form})
	output = template.render(variables)
	return HttpResponse(output)
	
	
def add_book(request):
    if request.method == 'POST':
        form = FormularzDodawaniaKsiazek(request.POST)
        if form.is_valid():
			books_book = Book(
				title = form.cleaned_data['title'],
				autor = form.cleaned_data['autor'],
				slug = form.cleaned_data['link'],
				#book_image = form.cleaned_data['image'],
				text = form.cleaned_data['description'],
				#categories = form.cleaned_data['category']
				price = form.cleaned_data['price'],
				quantity = form.cleaned_data['quantity'],
			)
			books_book.save()
			
			template = get_template("page/add_book_succes.html")    
			variables = RequestContext(request,{'form':form})
			output = template.render(variables)
			return HttpResponse(output)  
    else:
        form = FormularzDodawaniaKsiazek()    
    template = get_template("page/add_book.html")
    variables = RequestContext(request,{'form':form})
    output = template.render(variables)
    return HttpResponse(output)
	
	
def add_category(request):
    if request.method == 'POST':
        form = FormularzDodawaniaKategorii(request.POST)
        if form.is_valid():
			books_category = Book(
				title = form.cleaned_data['name'],
				#slug = form.cleaned_data['link'],
				#book_image = form.cleaned_data['image'],
			)
			books_category.save()
			template = get_template("page/add_category_succes.html")    
			variables = RequestContext(request,{'form':form})
			output = template.render(variables)
			return HttpResponse(output)    
    else:
        form = FormularzDodawaniaKategorii()    
    template = get_template("page/add_category.html")
    variables = RequestContext(request,{'form':form})
    output = template.render(variables)
    return HttpResponse(output)	
	
def contact(request):
	template = get_template("page/contact.html") #zbieżność nazw wzorca i funkcji nie ma żadnego znaczenia
	variables=RequestContext(request)
	output = template.render(variables)
	return HttpResponse(output)
	
def search(request):
	form = FormularzWyszukiwania(request.POST)
	template = get_template("page/search.html") #zbieżność nazw wzorca i funkcji nie ma żadnego znaczenia
	variables = RequestContext(request,{'form':form})
	output = template.render(variables)
	return HttpResponse(output)
	
def basket(request):
	template = get_template("page/basket.html") #zbieżność nazw wzorca i funkcji nie ma żadnego znaczenia
	variables=RequestContext(request)
	output = template.render(variables)
	return HttpResponse(output)	
	
class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class BookViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer	

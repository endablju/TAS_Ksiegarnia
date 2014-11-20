# -*- coding: utf-8 -*-

from django.contrib.auth import logout
from django.http import HttpResponse,HttpResponseRedirect
from django.template.loader import get_template
from django.template import RequestContext
from django.shortcuts import render_to_response
from books.models import *
from books.forms import *


def index(request):
    template = get_template("index.html") #zbieżność nazw wzorca i funkcji nie ma żadnego znaczenia
    variables=RequestContext(request)
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

	
    #return render_to_response('index.html',
     #       {'zmienna': 'Jestem widokiem'},
      #      context_instance=RequestContext(request))
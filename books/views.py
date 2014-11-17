# -*- coding: utf-8 -*-
from django.contrib.auth import logout
from django.http import HttpResponse
from django.template.loader import get_template
from django.template import RequestContext
from django.shortcuts import render_to_response
from books.models import *


def index(request):
    template = get_template("index.html") #zbieżność nazw wzorca i funkcji nie ma żadnego znaczenia
    variables=RequestContext(request)
    output = template.render(variables)
    return HttpResponse(output)
	
def register_page(request):
    template = get_template("register.html")
    form = FormularzRejestracji()
    variables = RequestContext(request,{'form':form})
    output = template.render(variables)
    return HttpResponse(output)

	
    #return render_to_response('index.html',
     #       {'zmienna': 'Jestem widokiem'},
      #      context_instance=RequestContext(request))
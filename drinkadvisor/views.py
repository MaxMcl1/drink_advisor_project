from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.

def index(request):
    

    response = render(request, 'drinkadvisor/index.html')

    
    return response

def about(request):
    

    response = render(request, 'drinkadvisor/about.html')

    
    return response

def drinks(request):
    

    response = render(request, 'drinkadvisor/drinks.html')

    
    return response

def sugar_free(request):
    

    response = render(request, 'drinkadvisor/sugar_free.html')

    
    return response

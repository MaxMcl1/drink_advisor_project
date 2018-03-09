from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.

def index(request):
    

    response = render(request, 'drinkadvisor/index.html')

    
    return response

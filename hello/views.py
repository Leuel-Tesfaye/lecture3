from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

#? creating a function that takes (request) as an argument : and this argument is going to represent
#? the HTTP request that the user made in order to access our web server

def index(request):
    # return HttpResponse("Hello, python !")
    return render (request, "hello/index.html")
def testing(request):
    return HttpResponse('This is testing another view function')

def routing(request):
    return HttpResponse("This message is response of routing function")


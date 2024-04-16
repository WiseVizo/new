from django.shortcuts import render, HttpResponse

# Create your views here.
def greet(request):
    return HttpResponse("Hello! Welcome to our food ordering platform.")
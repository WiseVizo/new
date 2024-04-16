from django.shortcuts import render, HttpResponse
from .models import Food
# Create your views here.
def greet(request):
    return HttpResponse("Hello! Welcome to our food ordering platform.")

def list_all_foods(request):
    food_list = Food.objects.all()
    return HttpResponse(food_list)
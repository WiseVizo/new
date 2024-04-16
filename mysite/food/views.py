from django.shortcuts import render, HttpResponse
from .models import Food
from django.template import loader
# Create your views here.
def greet(request):
    return HttpResponse("Hello! Welcome to our food ordering platform.")

def list_all_foods(request):
    food_list = Food.objects.all()
    template = loader.get_template("food/index.html")
    context = {
        "food_list" : food_list,
    }

    return HttpResponse(template.render(context, request))

def details(request, food_id):
    food = Food.objects.get(pk=food_id)
    context = {
        "food": food,
    }
    return render(request, "food/details.html", context)
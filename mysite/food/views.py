from django.shortcuts import redirect, render, HttpResponse
from .models import Food
from django.template import loader
from .forms import ItemForm
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

def create_item(request):
    form = ItemForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("food:list_all_foods")
    context = {
        'form': form,
    }
    return render(request, "food/item_form.html", context)

def update_item(request, food_id):
    item = Food.objects.get(pk=food_id)
    form = ItemForm(request.POST or None, instance=item)
    if form.is_valid():
        form.save()
        return redirect("food:list_all_foods")
    context = {
        'form': form,
        'item': item,
    }
    return render(request, "food/item_form.html", context)

def delete_item(request, food_id):
    item = Food.objects.get(pk=food_id)
    if request.method == 'POST':
        item.delete()
        return redirect("food:list_all_foods")

    return render(request, "food/remove_item.html", {'item':item})
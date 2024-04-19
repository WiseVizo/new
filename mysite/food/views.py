from django.shortcuts import redirect, render, HttpResponse
from .models import Food
from django.template import loader
from .forms import ItemForm
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.contrib.auth.models import User
# Create your views here.
def greet(request):
    return HttpResponse("Hello! Welcome to our food ordering platform.")

def list_all_foods(request): # also a food view but function based
    food_list = Food.objects.all()
    template = loader.get_template("food/index.html")
    context = {
        "food_list" : food_list,
    }

    return HttpResponse(template.render(context, request))

class FoodClassView(ListView):
    model = Food
    template_name = 'food/index.html'
    context_object_name = 'food_list'


def details(request, food_id):
    food = Food.objects.get(pk=food_id)
    context = {
        "food": food,
    }
    return render(request, "food/details.html", context)

class DetailsClassView(DetailView):
    # if any params like food_id in our case they need to go directly into urls
    model = Food
    template_name = "food/details.html" 
    # we don't need to pass context here just replace context_var name with object in html file

def create_item(request):
    form = ItemForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("food:list_all_foods")
    context = {
        'form': form,
    }
    return render(request, "food/item_form.html", context)

class CreateItemView(CreateView):
    model = Food
    fields = ["name", "description", "price", "image"]
    template_name = "food/item_form.html"

    def form_valid(self, form):
        form.instance.user_name = self.request.user
        return super().form_valid(form)

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
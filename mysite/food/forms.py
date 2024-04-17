from django import forms
from .models import Food

class ItemForm(forms.ModelForm):
    class Meta:
        model = Food
        fields = ["name", "description", "price", "image",]
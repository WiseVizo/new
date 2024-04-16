from django.urls import path
from . import views
urlpatterns = [
    path('', views.list_all_foods, name="list_all_foods"),
    path('<int:food_id>/', views.details, name="details"),
    path('greet/', views.greet, name="greet"),
]
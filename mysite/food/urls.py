from django.urls import path
from . import views
app_name = 'food'
urlpatterns = [
    path('', views.FoodClassView.as_view(), name="list_all_foods"), # class list view
    # path('', views.list_all_foods, name="list_all_foods"), # function view
    path('<int:pk>/', views.DetailsClassView.as_view(), name="details"), # class detail view
    # path('<int:food_id>/', views.details, name="details"), # function view
    path('greet/', views.greet, name="greet"),
    # for adding items
    path('add/', views.create_item, name="create_item"),
    #edit item
    path('update/<int:food_id>/', views.update_item, name="update_item"),
    #delete item
    path('delete/<int:food_id>/', views.delete_item, name="delete_item"),
]
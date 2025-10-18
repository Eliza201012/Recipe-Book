from django.urls import path
from . import views

urlpatterns = [
    path("create_recipe/", views.create_recipe, name="create_recipe"),
    path("recipe_list/", views.recipe_list, name="recipe_list"),
    path("recipe_detail/<int:pk>/", views.recipe_detail, name="recipe_detail"),
    path("recipe_update/<int:pk>/", views.recipe_update, name="recipe_update"),
    path("recipe_delete/<int:pk>/", views.recipe_delete, name="recipe_delete"),
]

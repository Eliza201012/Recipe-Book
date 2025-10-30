from django.urls import path
from . import views

urlpatterns = [
    # 🍴 Recipes
    path("", views.recipe_list, name="recipe_list"),
    path("create_recipe/", views.create_recipe, name="create_recipe"),
    path("recipe_detail/<int:pk>/", views.recipe_detail, name="recipe_detail"),
    path("recipe_update/<int:pk>/", views.recipe_update, name="recipe_update"),
    path("recipe_delete/<int:pk>/", views.recipe_delete, name="recipe_delete"),


    # 📚 Books
    path("books/", views.book_list, name="book_list"),
    path("books/create_book/", views.create_book, name="create_book"),
    path("books/book_detail/<int:pk>/", views.book_detail, name="book_detail"),
    path("books/book_update/<int:pk>/", views.book_update, name="book_update"),
    path("books/book_delete/<int:pk>/", views.book_delete, name="book_delete"),
]
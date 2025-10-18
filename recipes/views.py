from django.shortcuts import render, get_object_or_404, redirect
from .models import Recipe, Book
from .forms import RecipeForm, BookForm

# CREATE (Recipe)
def create_recipe(request):
    if request.method == "POST":
        form = RecipeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("recipes:recipe_list")
    else:
        form = RecipeForm()
    return render(request, "recipes/recipe_form.html", {"form" : form})

# READ (Recipe list)
def recipe_list(request):
    recipes = Recipe.objects.all()
    return render(request, "recipes/recipe_list.html", {"recipes" : recipes})

# READ (Recipe detail)
def recipe_detail(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    return render(request, "recipes/recipe_detail.html", {"recipe" : recipe})

# UPDATE
def recipe_update(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    if request.method == "POST":
        form = RecipeForm(request.POST, instance=Recipe)
        if form.is_valid():
            form.save()
            return redirect("recipes:recipe_list")
    else:
        form = RecipeForm(instance=Recipe)
    return render(request, "recipes/recipe_form.html", {"form" : form})

# DELETE
def recipe_delete(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    if request.method == "POST":
        recipe.delete()
        return redirect("recipes:recipe_list")
    return render(request, "recipes/recipe_confirm_delete.html", {"recipe" : recipe})
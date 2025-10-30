from django.shortcuts import render, get_object_or_404, redirect
from .models import Recipe, Book
from .forms import RecipeForm, BookForm
from django.contrib.auth.decorators import login_required

# CREATE (Recipe)
@login_required
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
@login_required
def recipe_list(request):
    recipes = Recipe.objects.all()
    return render(request, "recipes/recipe_list.html", {"recipes" : recipes})

# READ (Recipe detail)
@login_required
def recipe_detail(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    return render(request, "recipes/recipe_detail.html", {"recipe" : recipe})

# UPDATE (Recipe)
@login_required
def recipe_update(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    if request.method == "POST":
        form = RecipeForm(request.POST, instance=recipe)
        if form.is_valid():
            form.save()
            return redirect("recipes:recipe_list")
    else:
        form = RecipeForm(instance=recipe)
    return render(request, "recipes/recipe_form.html", {"form" : form})

# DELETE (Recipe)
@login_required
def recipe_delete(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    if request.method == "POST":
        recipe.delete()
        return redirect("recipes:recipe_list")
    return render(request, "recipes/recipe_confirm_delete.html", {"recipe" : recipe})



# CREATE (Book)
@login_required
def create_book(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("recipes:book_list")
    else:
        form = BookForm()
    return render(request, "recipes/book_form.html", {"form" : form})

# READ (Book list)
@login_required
def book_list(request):
    books = Book.objects.all()
    return render(request, "recipes/book_list.html", {"books" : books})

# READ (Book detail)
@login_required
def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(request, "recipes/book_detail.html", {"book" : book})

# UPDATE (Book)
@login_required
def book_update(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == "POST":
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect("recipes:book_list")
    else:
        form = BookForm(instance=book)
    return render(request, "recipes/book_form.html", {"form" : form})

# DELETE (Book)
@login_required
def book_delete(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == "POST":
        book.delete()
        return redirect("recipes:book_list")
    return render(request, "recipes/book_confirm_delete.html", {"book" : book})
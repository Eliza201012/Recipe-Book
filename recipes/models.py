from django.db import models

class Recipe(models.Model):
    CATEGORY_CHOICES = [
        ("breakfast", "Breakfast"),
        ("lunch", "Lunch"),
        ("dinner", "Dinner"),
        ("dessert", "Dessert"),
        ("drinks", "Drinks"),
        ("high-protein food", "High-protein food")
    ]
    title = models.CharField(verbose_name="Title", max_length=200)
    cooking_time = models.TimeField(verbose_name="Cooking time")
    description = models.TextField(verbose_name="Description")
    instructions = models.TextField(verbose_name="Steps one by one")
    category = models.CharField(verbose_name="Category", choices=CATEGORY_CHOICES, default="breakfast")
    created_at = models.DateField(verbose_name="Created at", auto_now_add=True)
    updated_at = models.DateField(verbose_name="Updated at", auto_now=True)

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Recipe"
        verbose_name_plural = "Recipes"


class Book(models.Model):
    title = models.CharField(verbose_name="Title", max_length=150)
    recipe = models.ForeignKey(Recipe, verbose_name="Recipe", on_delete=models.CASCADE, related_name="books")
    created_at = models.DateField(verbose_name="Created at", auto_now_add=True)
    updated_at = models.DateField(verbose_name="Updated at", auto_now=True)